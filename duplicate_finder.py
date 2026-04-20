# duplicate_finder.py

import os
import re

class DuplicateFinder:
    """Simple duplicate code finder."""
    
    def __init__(self, project_path):
        # Store the root folder we want to scan.
        self.project_path = project_path
        # List of file paths that match our file types.
        self.code_files = []
        # Detected duplicates will be stored here.
        self.duplicates = []
    
    def run(self):
        """Run the complete duplicate detection workflow."""
        print("🔍 Starting duplicate code analysis...\n")
        
        # Step 1: Find all candidate files in the project.
        print("📁 Scanning for TypeScript/JavaScript files...")
        self.code_files = self.scan_files()
        print(f"   Found {len(self.code_files)} files\n")
        
        # Step 2: Analyze the discovered files for exact duplicates.
        print("🔎 Analyzing code for duplicates...")
        self.duplicates = self.find_duplicates()
        print(f"   Found {len(self.duplicates)} duplicates\n")
        
        # Step 3: Build the final report string.
        print("📊 Generating report...\n")
        report = self.generate_report()
        
        return report
    
    def scan_files(self):
        """Find all TypeScript/JavaScript files under the project folder."""
        files = []

        # os.walk() traverses the directory tree from top to bottom.
        for root, dirs, filenames in os.walk(self.project_path):
            # Remove directories we do not want to enter.
            # Modifying dirs in place prevents os.walk from descending into them.
            dirs[:] = [
                d for d in dirs
                if d not in ['node_modules', '.git', '__pycache__', 'venv', 'dist', 'build', '.next']
            ]
            
            # Keep only the file types we care about for duplicate detection.
            for filename in filenames:
                if filename.endswith(('.ts', '.tsx', '.js', '.jsx')):
                    files.append(os.path.join(root, filename))
        
        return files
    
    def read_file(self, path):
        """Read the full contents of a file and return it as a string."""
        with open(path, 'r') as f:
            return f.read()
    
    def normalize(self, code):
        """Normalize code so equivalent files compare equally."""
        lines = []

        # Process the file one line at a time.
        for line in code.split('\n'):
            stripped = line.strip()
            # Skip full-line single-line comments.
            if stripped.startswith('//'):
                continue
            # If there is an inline // comment, remove it.
            if '//' in line:
                line = line.split('//')[0]
            lines.append(line)
        
        # Reassemble the lines into a single string before removing block comments.
        code = '\n'.join(lines)
        
        # Remove multi-line comments like /* comment */.
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
        
        # Normalize whitespace by collapsing all whitespace sequences into a single space.
        # This makes formatting differences irrelevant for duplicate detection.
        return ' '.join(code.split())
    
    def find_duplicates(self):
        """Compare normalized file contents and collect exact duplicates."""
        seen = {}
        duplicates = []
        
        for file_path in self.code_files:
            code = self.read_file(file_path)
            normalized = self.normalize(code)
            
            # If we have already seen the same normalized code, it is a duplicate.
            if normalized in seen:
                duplicates.append({
                    'original': seen[normalized],
                    'duplicate': file_path,
                    'code': code
                })
            else:
                # Store the first occurrence of this normalized content.
                seen[normalized] = file_path
        
        return duplicates
    
    def generate_report(self):
        """Create a human-readable report from the duplicate list."""
        if not self.duplicates:
            return "✅ No duplicates found!"
        
        report = ["=" * 60]
        report.append("🔍 DUPLICATE CODE REPORT")
        report.append("=" * 60)
        report.append(f"\nFound {len(self.duplicates)} duplicate(s)\n")
        
        # Include the original and duplicate file paths, plus a code preview.
        for i, dup in enumerate(self.duplicates, 1):
            report.append(f"\n--- Duplicate #{i} ---")
            report.append(f"📄 Original: {dup['original']}")
            report.append(f"📄 Copy:     {dup['duplicate']}")
            report.append(f"\n📝 Code Preview:")
            preview = dup['code'][:200] + "..." if len(dup['code']) > 200 else dup['code']
            report.append(preview)
            report.append("-" * 60)
        
        return '\n'.join(report)


# Main program
if __name__ == "__main__":
    # Set the project root to scan. This script currently scans only the Sptinder repository.
    project_path = "/Users/ben.conlon/Projects/Sptinder"
    
    # Create the finder instance and run the analysis.
    finder = DuplicateFinder(project_path)
    report = finder.run()
    
    # Output the final report to the terminal.
    print(report)
