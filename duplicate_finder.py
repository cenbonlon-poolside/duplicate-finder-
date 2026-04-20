# duplicate_finder.py

import os

class DuplicateFinder:
    """Simple duplicate code finder"""
    
    def __init__(self, project_path):
        self.project_path = project_path
        self.code_files = []
        self.duplicates = []
    
    def run(self):
        """Run the complete analysis"""
        print("🔍 Starting duplicate code analysis...\n")
        
        # Step 1: Find files
        print("📁 Scanning for TypeScript/JavaScript files...")
        self.code_files = self.scan_files()
        print(f"   Found {len(self.code_files)} files\n")
        
        # Step 2: Find duplicates
        print("🔎 Analyzing code for duplicates...")
        self.duplicates = self.find_duplicates()
        print(f"   Found {len(self.duplicates)} duplicates\n")
        
        # Step 3: Generate report
        print("📊 Generating report...\n")
        report = self.generate_report()
        
        return report
    
    def scan_files(self):
        """Find all TypeScript/JavaScript files"""
        files = []
        for root, dirs, filenames in os.walk(self.project_path):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '__pycache__', 'venv', 'dist', 'build', '.next']]
            
            for filename in filenames:
                if filename.endswith(('.ts', '.tsx', '.js', '.jsx')):
                    files.append(os.path.join(root, filename))
        
        return files
    
    def read_file(self, path):
        """Read file content"""
        with open(path, 'r') as f:
            return f.read()
    
    def normalize(self, code):
        """Clean code for comparison"""
        lines = []
        for line in code.split('\n'):
            # Skip single-line comments
            if line.strip().startswith('//'):
                continue
            # Remove inline comments
            if '//' in line:
                line = line.split('//')[0]
            lines.append(line)
        
        # Join and remove whitespace
        code = '\n'.join(lines)
        
        # Remove multi-line comments /* */
        import re
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
        
        # Remove extra whitespace
        return ' '.join(code.split())
    
    def find_duplicates(self):
        """Find duplicate files"""
        seen = {}
        duplicates = []
        
        for file_path in self.code_files:
            code = self.read_file(file_path)
            normalized = self.normalize(code)
            
            if normalized in seen:
                duplicates.append({
                    'original': seen[normalized],
                    'duplicate': file_path,
                    'code': code
                })
            else:
                seen[normalized] = file_path
        
        return duplicates
    
    def generate_report(self):
        """Create formatted report"""
        if not self.duplicates:
            return "✅ No duplicates found!"
        
        report = ["=" * 60]
        report.append("🔍 DUPLICATE CODE REPORT")
        report.append("=" * 60)
        report.append(f"\nFound {len(self.duplicates)} duplicate(s)\n")
        
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
    # Set your project path - scanning just Sptinder
    project_path = "/Users/ben.conlon/Projects/Sptinder"  # Just this project
    
    # Create and run finder
    finder = DuplicateFinder(project_path)
    report = finder.run()
    
    # Print report
    print(report)