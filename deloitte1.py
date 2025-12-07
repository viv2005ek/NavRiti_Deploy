import json
from datetime import datetime
from typing import Dict, List, Any
import os
import re

# PDF Processing Libraries
try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("⚠️  PyPDF2 not installed. Run: pip install PyPDF2")

try:
    import pdfplumber
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False
    print("⚠️  pdfplumber not installed. Run: pip install pdfplumber")

class NaviRitiCareerPredictor:
    """
    NaviRiti Career Prediction System - Enhanced Version
    Features: Grade/Degree Selection, Enhanced PDF CV Parsing with JSON Export
    """
    
    def __init__(self):
        self.career_database = self._initialize_career_database()
        self.skill_requirements = self._initialize_skill_requirements()
        self.psychometric_test_urls = self._initialize_psychometric_resources()
        self.degree_options = self._initialize_degree_options()
        
    def _initialize_degree_options(self) -> List[str]:
        """Initialize undergraduate degree options"""
        return [
            'B.Tech/B.E. (Computer Science)',
            'B.Tech/B.E. (Mechanical)',
            'B.Tech/B.E. (Electrical)',
            'B.Tech/B.E. (Civil)',
            'B.Tech/B.E. (Electronics)',
            'B.Tech/B.E. (Chemical)',
            'B.Com (Commerce)',
            'BBA (Business Administration)',
            'BCA (Computer Applications)',
            'B.Sc (Science)',
            'BA (Arts/Humanities)',
            'MBBS (Medical)',
            'B.Pharm (Pharmacy)',
            'LLB (Law)',
            'B.Des (Design)',
            'MBA',
            'M.Tech',
            'M.Sc',
            'Other'
        ]
    
    def _initialize_career_database(self) -> Dict:
        """Initialize comprehensive career database"""
        return {
            'Technology': ['Software Engineer', 'Data Scientist', 'AI/ML Engineer', 'Cybersecurity Analyst', 
                          'Full Stack Developer', 'DevOps Engineer', 'Cloud Architect', 'Game Developer'],
            'Medical': ['Doctor (MBBS)', 'Surgeon', 'Dentist', 'Physiotherapist', 'Pharmacist', 
                       'Nursing', 'Medical Research', 'Public Health Specialist'],
            'Engineering': ['Mechanical Engineer', 'Civil Engineer', 'Electrical Engineer', 'Chemical Engineer',
                           'Aerospace Engineer', 'Automotive Engineer', 'Biomedical Engineer'],
            'Business': ['Investment Banker', 'Financial Analyst', 'Management Consultant', 'Entrepreneur',
                        'Marketing Manager', 'Business Analyst', 'Product Manager'],
            'Creative': ['Graphic Designer', 'UI/UX Designer', 'Fashion Designer', 'Animator', 
                        'Content Creator', 'Photographer', 'Video Editor', 'Architect'],
            'Arts': ['Musician', 'Dancer', 'Actor', 'Writer', 'Journalist', 'Fine Artist', 'Film Director'],
            'Social': ['Psychologist', 'Social Worker', 'NGO Manager', 'HR Manager', 'Teacher', 
                      'Counselor', 'Public Relations'],
            'Law': ['Lawyer', 'Judge', 'Legal Advisor', 'Corporate Lawyer', 'Human Rights Lawyer'],
            'Science': ['Research Scientist', 'Biotechnologist', 'Environmental Scientist', 'Astronomer',
                       'Physicist', 'Chemist', 'Mathematician'],
            'Sports': ['Professional Athlete', 'Sports Coach', 'Sports Manager', 'Physiotherapist',
                      'Fitness Trainer', 'Sports Nutritionist']
        }
    
    def _initialize_skill_requirements(self) -> Dict:
        """Initialize skill requirements for different careers"""
        return {
            'Software Engineer': ['Programming', 'Problem Solving', 'Data Structures', 'Algorithms', 'Git'],
            'Data Scientist': ['Python', 'Statistics', 'Machine Learning', 'SQL', 'Data Visualization'],
            'Doctor (MBBS)': ['Biology', 'Chemistry', 'Empathy', 'Communication', 'Critical Thinking'],
            'Financial Analyst': ['Accounting', 'Excel', 'Financial Modeling', 'Analytics', 'Communication'],
            'Graphic Designer': ['Adobe Suite', 'Creativity', 'Visual Design', 'Typography', 'Color Theory'],
            'Lawyer': ['Legal Knowledge', 'Communication', 'Research', 'Critical Thinking', 'Writing'],
            'Teacher': ['Subject Knowledge', 'Communication', 'Patience', 'Creativity', 'Leadership'],
            'Mechanical Engineer': ['CAD', 'Thermodynamics', 'Mechanics', 'Problem Solving', 'AutoCAD'],
            'Business Analyst': ['Excel', 'SQL', 'Data Analysis', 'Communication', 'Business Strategy'],
            'Content Creator': ['Creativity', 'Video Editing', 'Social Media', 'Communication', 'Marketing']
        }
    
    def _initialize_psychometric_resources(self) -> Dict:
        """Initialize external psychometric test resources"""
        return {
            'stage1': {
                'personality': [
                    {'name': '16Personalities', 'url': 'https://www.16personalities.com/', 
                     'description': 'Free personality test based on Myers-Briggs'},
                    {'name': 'OpenPsychometrics', 'url': 'https://openpsychometrics.org/', 
                     'description': 'Multiple free personality tests'},
                    {'name': 'Truity Career Personality Test', 'url': 'https://www.truity.com/test/type-finder-personality-test-new',
                     'description': 'Career-focused personality assessment'}
                ],
                'interests': [
                    {'name': 'Career Explorer Holland Code', 'url': 'https://www.careerexplorer.com/career-test/',
                     'description': 'Holland Code (RIASEC) interest assessment'},
                    {'name': 'MyPlan Interest Assessment', 'url': 'https://www.myplan.com/assess/interest-assessment.php',
                     'description': 'Interest profiler for career exploration'}
                ]
            },
            'stage2': {
                'aptitude': [
                    {'name': 'YouScience Aptitude Test', 'url': 'https://www.youscience.com/',
                     'description': 'Comprehensive aptitude assessment'},
                    {'name': 'Practice Aptitude Tests', 'url': 'https://www.practiceaptitudetests.com/',
                     'description': 'Numerical, Verbal, Logical reasoning tests'},
                    {'name': 'AssessmentDay', 'url': 'https://www.assessmentday.co.uk/',
                     'description': 'Aptitude tests for careers'}
                ],
                'career_interest': [
                    {'name': 'O*NET Interest Profiler', 'url': 'https://www.mynextmove.org/explore/ip',
                     'description': 'Official US career interest assessment'},
                    {'name': 'Career One Stop', 'url': 'https://www.careeronestop.org/toolkit/careers/interest-assessment.aspx',
                     'description': 'Government career interest profiler'}
                ]
            },
            'stage3': {
                'professional': [
                    {'name': 'DISC Personality Test', 'url': 'https://www.123test.com/disc-personality-test/',
                     'description': 'Workplace personality assessment'},
                    {'name': 'CliftonStrengths', 'url': 'https://www.gallup.com/cliftonstrengths/',
                     'description': 'Identify your top talents (paid)'},
                    {'name': 'Skills Matcher', 'url': 'https://nationalcareers.service.gov.uk/skills-assessment',
                     'description': 'Skills assessment for career matching'}
                ]
            }
        }
    
    # ==================== ENHANCED PDF CV PARSING ====================
    
    def parse_cv_pdf(self, pdf_path: str) -> Dict:
        """Enhanced CV parsing with comprehensive extraction"""
        print(f"\n📄 Parsing CV from: {pdf_path}")
        
        if not os.path.exists(pdf_path):
            print(f"❌ Error: File not found at {pdf_path}")
            return {}
        
        cv_data = {
            'raw_text': '',
            'name': '',
            'email': '',
            'phone': '',
            'linkedin': '',
            'github': '',
            'portfolio': '',
            'education': [],
            'experience': [],
            'skills': [],
            'technical_skills': [],
            'soft_skills': [],
            'projects': [],
            'certifications': [],
            'achievements': [],
            'languages': [],
            'parsed_successfully': False,
            'parsed_at': datetime.now().isoformat()
        }
        
        try:
            if PDFPLUMBER_AVAILABLE:
                cv_data = self._parse_with_pdfplumber(pdf_path, cv_data)
            elif PDF_AVAILABLE:
                cv_data = self._parse_with_pypdf2(pdf_path, cv_data)
            else:
                print("❌ No PDF library available. Install PyPDF2 or pdfplumber")
                return cv_data
            
            if cv_data['raw_text']:
                cv_data = self._extract_cv_information_enhanced(cv_data)
                cv_data['parsed_successfully'] = True
                
                # Save extracted data to JSON
                json_filename = self._save_cv_data_to_json(pdf_path, cv_data)
                cv_data['saved_json'] = json_filename
                
                print("✅ CV parsed successfully!")
                print(f"📊 Extracted: {len(cv_data['skills'])} skills, {len(cv_data['experience'])} experiences, {len(cv_data['projects'])} projects")
            
        except Exception as e:
            print(f"❌ Error parsing CV: {str(e)}")
        
        return cv_data
    
    def _save_cv_data_to_json(self, pdf_path: str, cv_data: Dict) -> str:
        """Save extracted CV data to JSON file with same name as PDF"""
        # Get PDF filename without extension
        base_name = os.path.splitext(pdf_path)[0]
        json_filename = f"{base_name}_extracted.json"
        
        # Create a clean copy without raw_text for better readability
        clean_data = {k: v for k, v in cv_data.items() if k != 'raw_text'}
        
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(clean_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Extracted CV data saved to: {json_filename}")
        return json_filename
    
    def _parse_with_pdfplumber(self, pdf_path: str, cv_data: Dict) -> Dict:
        """Parse PDF using pdfplumber"""
        import pdfplumber
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    cv_data['raw_text'] += text + "\n"
        
        return cv_data
    
    def _parse_with_pypdf2(self, pdf_path: str, cv_data: Dict) -> Dict:
        """Parse PDF using PyPDF2"""
        import PyPDF2
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    cv_data['raw_text'] += text + "\n"
        
        return cv_data
    
    def _extract_cv_information_enhanced(self, cv_data: Dict) -> Dict:
        """Enhanced extraction of structured information from CV text"""
        text = cv_data['raw_text']
        lines = text.split('\n')
        text_lower = text.lower()
        
        # Extract email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        if emails:
            cv_data['email'] = emails[0]
        
        # Extract phone
        phone_pattern = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
        phones = re.findall(phone_pattern, text)
        if phones:
            cv_data['phone'] = phones[0].strip()
        
        # Extract LinkedIn
        linkedin_pattern = r'linkedin\.com/in/[\w-]+'
        linkedin = re.findall(linkedin_pattern, text_lower)
        if linkedin:
            cv_data['linkedin'] = linkedin[0]
        
        # Extract GitHub
        github_pattern = r'github\.com/[\w-]+'
        github = re.findall(github_pattern, text_lower)
        if github:
            cv_data['github'] = github[0]
        
        # Extract portfolio/website
        url_pattern = r'https?://(?:www\.)?[\w\-\.]+\.[\w]{2,}'
        urls = re.findall(url_pattern, text)
        for url in urls:
            if 'linkedin' not in url.lower() and 'github' not in url.lower():
                cv_data['portfolio'] = url
                break
        
        # Extract name (improved)
        for line in lines[:10]:
            line_clean = line.strip()
            if len(line_clean) > 0 and 2 <= len(line_clean.split()) <= 5:
                if not any(char.isdigit() for char in line_clean) and '@' not in line_clean:
                    if not any(keyword in line_clean.lower() for keyword in ['resume', 'cv', 'curriculum', 'profile']):
                        cv_data['name'] = line_clean
                        break
        
        # Enhanced Technical Skills Extraction
        technical_keywords = [
            # Programming Languages
            'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'swift', 'kotlin',
            # Web Technologies
            'html', 'css', 'react', 'angular', 'vue', 'nodejs', 'express', 'django', 'flask', 'spring', 'asp.net',
            # Databases
            'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'oracle', 'sqlite', 'cassandra',
            # Cloud & DevOps
            'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git', 'gitlab', 'terraform', 'ansible',
            # Data Science & ML
            'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy',
            'data analysis', 'data visualization', 'tableau', 'power bi', 'matplotlib', 'seaborn',
            # Tools
            'excel', 'powerpoint', 'jira', 'confluence', 'figma', 'adobe photoshop', 'adobe illustrator',
            # Frameworks
            'restful api', 'graphql', 'microservices', 'agile', 'scrum', 'ci/cd'
        ]
        
        for skill in technical_keywords:
            if skill in text_lower:
                cv_data['technical_skills'].append(skill.title())
        
        # Soft Skills Extraction
        soft_skill_keywords = [
            'leadership', 'communication', 'teamwork', 'problem solving', 'critical thinking',
            'time management', 'project management', 'analytical', 'creative', 'adaptable',
            'collaboration', 'presentation', 'negotiation', 'conflict resolution'
        ]
        
        for skill in soft_skill_keywords:
            if skill in text_lower:
                cv_data['soft_skills'].append(skill.title())
        
        # Combined skills list
        cv_data['skills'] = cv_data['technical_skills'] + cv_data['soft_skills']
        
        # Enhanced Education Extraction
        education_keywords = [
            'B.Tech', 'B.E.', 'M.Tech', 'MBA', 'B.Sc', 'M.Sc', 'B.Com', 'BBA', 'BCA',
            'Bachelor', 'Master', 'CGPA', 'GPA', 'Percentage', 'University', 'College', 'Institute'
        ]
        
        for i, line in enumerate(lines):
            for keyword in education_keywords:
                if keyword.lower() in line.lower() and len(line.strip()) > 5:
                    # Try to capture next line as well for complete info
                    edu_entry = line.strip()
                    if i + 1 < len(lines) and len(lines[i + 1].strip()) > 0:
                        edu_entry += " | " + lines[i + 1].strip()
                    cv_data['education'].append(edu_entry)
                    break
        
        # Enhanced Experience Extraction
        experience_keywords = [
            'intern', 'engineer', 'developer', 'analyst', 'manager', 'consultant', 
            'assistant', 'associate', 'specialist', 'coordinator', 'lead', 'senior',
            'junior', 'trainee', 'executive'
        ]
        year_pattern = r'20\d{2}|19\d{2}'
        
        for i, line in enumerate(lines):
            if any(keyword in line.lower() for keyword in experience_keywords):
                if re.search(year_pattern, line) or (i > 0 and re.search(year_pattern, lines[i - 1])):
                    exp_entry = line.strip()
                    # Capture description lines
                    desc_lines = []
                    for j in range(i + 1, min(i + 4, len(lines))):
                        if lines[j].strip() and not any(kw in lines[j].lower() for kw in experience_keywords):
                            desc_lines.append(lines[j].strip())
                        else:
                            break
                    if desc_lines:
                        exp_entry += " | " + " ".join(desc_lines)
                    cv_data['experience'].append(exp_entry)
        
        # Enhanced Projects Extraction
        project_indicators = ['project', 'developed', 'built', 'created', 'implemented', 'designed']
        for i, line in enumerate(lines):
            if any(indicator in line.lower() for indicator in project_indicators):
                project_entry = line.strip()
                # Get tech stack and description
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line and len(next_line) > 10:
                        project_entry += " | " + next_line
                cv_data['projects'].append(project_entry)
        
        # Certifications Extraction
        cert_keywords = ['certified', 'certification', 'certificate', 'course', 'completed']
        for line in lines:
            if any(keyword in line.lower() for keyword in cert_keywords) and len(line.strip()) > 5:
                cv_data['certifications'].append(line.strip())
        
        # Achievements Extraction
        achievement_keywords = ['award', 'achievement', 'won', 'winner', 'ranked', 'scholarship', 'honor']
        for line in lines:
            if any(keyword in line.lower() for keyword in achievement_keywords) and len(line.strip()) > 5:
                cv_data['achievements'].append(line.strip())
        
        # Languages Extraction
        language_keywords = ['english', 'hindi', 'spanish', 'french', 'german', 'mandarin', 'japanese']
        for lang in language_keywords:
            if lang in text_lower:
                cv_data['languages'].append(lang.title())
        
        # Remove duplicates and limit entries
        cv_data['technical_skills'] = list(dict.fromkeys(cv_data['technical_skills']))
        cv_data['soft_skills'] = list(dict.fromkeys(cv_data['soft_skills']))
        cv_data['skills'] = list(dict.fromkeys(cv_data['skills']))
        cv_data['education'] = list(dict.fromkeys(cv_data['education']))[:5]
        cv_data['experience'] = list(dict.fromkeys(cv_data['experience']))[:10]
        cv_data['projects'] = list(dict.fromkeys(cv_data['projects']))[:10]
        cv_data['certifications'] = list(dict.fromkeys(cv_data['certifications']))[:10]
        cv_data['achievements'] = list(dict.fromkeys(cv_data['achievements']))[:10]
        cv_data['languages'] = list(dict.fromkeys(cv_data['languages']))
        
        return cv_data
    
    # ==================== GRADE/DEGREE SELECTION ====================
    
    def get_student_stage_input(self) -> tuple:
        """Get student stage with proper validation"""
        print("\n" + "="*80)
        print("📚 STUDENT INFORMATION")
        print("="*80)
        
        while True:
            print("\nAre you currently:")
            print("1. In School (Classes 6-12)")
            print("2. In College/University (Undergraduate/Postgraduate)")
            
            choice = input("\nEnter choice (1 or 2): ").strip()
            
            if choice == '1':
                # School student
                while True:
                    try:
                        grade = int(input("\nEnter your current class (6-12): ").strip())
                        if 6 <= grade <= 12:
                            stage = self.get_student_stage(grade)
                            return stage, grade, None
                        else:
                            print("❌ Invalid! Please enter a class between 6 and 12.")
                    except ValueError:
                        print("❌ Invalid input! Please enter a number.")
            
            elif choice == '2':
                # College/University student
                print("\n📚 SELECT YOUR DEGREE:")
                print("="*60)
                for idx, degree in enumerate(self.degree_options, 1):
                    print(f"{idx}. {degree}")
                print("="*60)
                
                while True:
                    try:
                        degree_choice = int(input("\nEnter degree number: ").strip())
                        if 1 <= degree_choice <= len(self.degree_options):
                            selected_degree = self.degree_options[degree_choice - 1]
                            
                            if selected_degree == 'Other':
                                selected_degree = input("Please specify your degree: ").strip()
                            
                            stage = "Stage 3: Undergraduate"
                            return stage, None, selected_degree
                        else:
                            print(f"❌ Invalid! Please enter a number between 1 and {len(self.degree_options)}.")
                    except ValueError:
                        print("❌ Invalid input! Please enter a number.")
            
            else:
                print("❌ Invalid choice! Please enter 1 or 2.")
    
    def get_student_stage(self, grade: int) -> str:
        """Determine student's academic stage"""
        if 6 <= grade <= 9:
            return "Stage 1: Exploration Years"
        elif 10 <= grade <= 12:
            return "Stage 2: Decision Years"
        else:
            return "Unknown Stage "
    
    # ==================== PSYCHOMETRIC TEST INTEGRATION ====================
    
    def display_psychometric_resources(self, stage: str):
        """Display external psychometric test resources"""
        stage_key = stage.lower().replace('stage ', 'stage').replace(':', '').strip()
        
        if 'stage 1' in stage_key or 'exploration' in stage_key:
            tests = self.psychometric_test_urls['stage1']
        elif 'stage 2' in stage_key or 'decision' in stage_key:
            tests = self.psychometric_test_urls['stage2']
        elif 'stage 3' in stage_key or 'undergraduate' in stage_key:
            tests = self.psychometric_test_urls['stage3']
        else:
            tests = {}
        
        print("\n" + "="*80)
        print("🧪 RECOMMENDED PSYCHOMETRIC TESTS (External)")
        print("="*80)
        
        for category, test_list in tests.items():
            print(f"\n📊 {category.upper().replace('_', ' ')} TESTS:")
            print("─"*80)
            for idx, test in enumerate(test_list, 1):
                print(f"\n{idx}. {test['name']}")
                print(f"   URL: {test['url']}")
                print(f"   Description: {test['description']}")
        
        print("\n" + "─"*80)
        print("💡 INSTRUCTIONS:")
        print("   1. Visit the URLs above and complete the tests")
        print("   2. Save/screenshot your results")
        print("   3. Return here to input your test scores")
        print("="*80)
    
    def collect_psychometric_results(self, stage: str) -> Dict:
        """Collect psychometric test results"""
        results = {}
        
        print("\n🧪 PSYCHOMETRIC TEST RESULTS INPUT")
        print("─"*80)
        print("Have you completed any external psychometric tests?")
        completed = input("Enter 'yes' if completed, 'no' to skip for now: ").lower()
        
        if completed != 'yes':
            print("\n⚠️  We recommend completing at least one test for better predictions.")
            print("You can continue without it, but results will be less accurate.\n")
            use_manual = input("Continue without test results? (yes/no): ").lower()
            if use_manual != 'yes':
                self.display_psychometric_resources(stage)
                return self.collect_psychometric_results(stage)
            else:
                return self._collect_manual_psychometric_input(stage)
        
        print("\n📋 Enter your test results:")
        
        if 'Stage 1' in stage:
            results = self._collect_stage1_psychometric()
        elif 'Stage 2' in stage:
            results = self._collect_stage2_psychometric()
        elif 'Stage 3' in stage:
            results = self._collect_stage3_psychometric()
        
        return results
    
    def _collect_manual_psychometric_input(self, stage: str) -> Dict:
        """Collect manual psychometric inputs"""
        print("\n📝 Manual Input Mode - Please rate yourself honestly")
        results = {}
        
        if 'Stage 1' in stage:
            print("\nPersonality Type (e.g., Creative, Analytical, Social, Practical):")
            results['personality_type'] = input("Your answer: ").strip()
            
            print("\nStrong Traits (rate 1-10 for each):")
            results['creativity'] = int(input("  Creativity (1-10): ") or 5)
            results['logical_thinking'] = int(input("  Logical Thinking (1-10): ") or 5)
            results['social_skills'] = int(input("  Social Skills (1-10): ") or 5)
            results['leadership'] = int(input("  Leadership (1-10): ") or 5)
            
        elif 'Stage 2' in stage:
            print("\nAptitude Scores (0-100):")
            results['logical_reasoning'] = float(input("  Logical Reasoning: ") or 50)
            results['verbal_ability'] = float(input("  Verbal Ability: ") or 50)
            results['numerical_ability'] = float(input("  Numerical Ability: ") or 50)
            results['spatial_reasoning'] = float(input("  Spatial Reasoning: ") or 50)
            
            print("\nPersonality Type:")
            results['personality_type'] = input("Type: ").strip()
            
        elif 'Stage 3' in stage:
            print("\nProfessional Aptitudes (0-100):")
            results['leadership_score'] = float(input("  Leadership: ") or 50)
            results['technical_aptitude'] = float(input("  Technical Aptitude: ") or 50)
            results['creative_thinking'] = float(input("  Creative Thinking: ") or 50)
            results['analytical_skills'] = float(input("  Analytical Skills: ") or 50)
            results['communication'] = float(input("  Communication: ") or 50)
        
        results['source'] = 'Manual Input'
        return results
    
    def _collect_stage1_psychometric(self) -> Dict:
        """Collect Stage 1 psychometric results"""
        results = {}
        
        print("\nWhich test(s) did you complete?")
        print("1. 16Personalities / Myers-Briggs Type")
        print("2. Holland Code (RIASEC)")
        print("3. Other personality/interest test")
        
        test_type = input("\nEnter choice (1/2/3): ").strip()
        
        if test_type == '1':
            print("\nWhat was your personality type? (e.g., INTJ, ENFP, ISTJ)")
            results['mbti_type'] = input("Type: ").strip().upper()
            results['personality_type'] = self._map_mbti_to_traits(results['mbti_type'])
        
        elif test_type == '2':
            print("\nEnter your Holland Code scores (0-100 for each):")
            results['realistic'] = float(input("  Realistic (hands-on, mechanical): ") or 50)
            results['investigative'] = float(input("  Investigative (analytical, scientific): ") or 50)
            results['artistic'] = float(input("  Artistic (creative, expressive): ") or 50)
            results['social'] = float(input("  Social (helping, teaching): ") or 50)
            results['enterprising'] = float(input("  Enterprising (leadership, business): ") or 50)
            results['conventional'] = float(input("  Conventional (organized, detailed): ") or 50)
        
        else:
            results = self._collect_manual_psychometric_input('Stage 1')
        
        print("\nTop Interest Areas from test (comma-separated):")
        interests = input("Areas: ").split(',')
        results['interest_areas'] = [i.strip() for i in interests if i.strip()]
        
        results['source'] = 'External Test'
        return results
    
    def _collect_stage2_psychometric(self) -> Dict:
        """Collect Stage 2 psychometric results"""
        results = {}
        
        print("\nEnter Aptitude Test Scores (0-100):")
        results['logical_reasoning'] = float(input("  Logical Reasoning: ") or 50)
        results['verbal_ability'] = float(input("  Verbal Ability: ") or 50)
        results['numerical_ability'] = float(input("  Numerical Ability: ") or 50)
        results['spatial_reasoning'] = float(input("  Spatial Reasoning: ") or 50)
        results['abstract_reasoning'] = float(input("  Abstract Reasoning: ") or 50)
        
        print("\nCareer Interest Assessment Results:")
        print("Top 3 career interest areas from your test (comma-separated):")
        interests = input("Areas: ").split(',')
        results['career_interests'] = [i.strip() for i in interests if i.strip()]
        
        print("\nPersonality Type from test:")
        results['personality_type'] = input("Type: ").strip()
        
        results['source'] = 'External Test'
        return results
    
    def _collect_stage3_psychometric(self) -> Dict:
        """Collect Stage 3 psychometric results"""
        results = {}
        
        print("\nProfessional Aptitude Scores (0-100):")
        results['leadership_score'] = float(input("  Leadership: ") or 50)
        results['technical_aptitude'] = float(input("  Technical Aptitude: ") or 50)
        results['creative_thinking'] = float(input("  Creative Thinking: ") or 50)
        results['analytical_skills'] = float(input("  Analytical Skills: ") or 50)
        results['communication'] = float(input("  Communication: ") or 50)
        results['teamwork'] = float(input("  Teamwork: ") or 50)
        results['problem_solving'] = float(input("  Problem Solving: ") or 50)
        
        print("\nWork Style Preferences from test:")
        print("(e.g., Independent, Collaborative, Strategic, Detail-oriented)")
        results['work_style'] = input("Your style: ").strip()
        
        results['source'] = 'External Test'
        return results
    
    def _map_mbti_to_traits(self, mbti_type: str) -> str:
        """Map MBTI type to traits"""
        mapping = {
            'INTJ': 'Analytical Strategist', 'INTP': 'Logical Thinker',
            'ENTJ': 'Strategic Leader', 'ENTP': 'Innovative Debater',
            'INFJ': 'Insightful Counselor', 'INFP': 'Idealistic Helper',
            'ENFJ': 'Inspiring Teacher', 'ENFP': 'Enthusiastic Motivator',
            'ISTJ': 'Organized Implementer', 'ISFJ': 'Supportive Protector',
            'ESTJ': 'Efficient Organizer', 'ESFJ': 'Helpful Supporter',
            'ISTP': 'Practical Problem-Solver', 'ISFP': 'Artistic Creator',
            'ESTP': 'Energetic Doer', 'ESFP': 'Spontaneous Entertainer'
        }
        return mapping.get(mbti_type, 'Unique Individual')
    
    def get_student_stage(self, grade: int) -> str:
        """Determine student's academic stage"""
        if 6 <= grade <= 9:
            return "Stage 1: Exploration Years"
        elif 10 <= grade <= 12:
            return "Stage 2: Decision Years"
        elif grade > 12:
            return "Stage 3: Undergraduate"
        else:
            return "Unknown Stage"
    
    # ==================== STAGE 1: EXPLORATION YEARS ====================
    
    def collect_stage1_inputs(self) -> Dict:
        """Collect Stage 1 inputs"""
        print("\n" + "="*70)
        print("📚 STAGE 1: EXPLORATION YEARS (CLASSES 6-9)")
        print("="*70)
        
        inputs = {}
        
        print("\n1️⃣ SUBJECT PREFERENCES")
        print("Available: Mathematics, Science, English, Social Studies,")
        print("           Computer Science, Arts, Languages, Physical Education")
        subjects = input("Enter subjects you enjoy (comma-separated): ").split(',')
        inputs['subject_preferences'] = [s.strip() for s in subjects if s.strip()]
        
        print("\n2️⃣ EXTRACURRICULAR ACTIVITIES")
        print("Options: Sports, Arts, Music, Drama, Coding, Debates, Dance, Robotics")
        activities = input("Enter activities (comma-separated): ").split(',')
        inputs['extracurricular_activities'] = [a.strip() for a in activities if a.strip()]
        
        print("\n3️⃣ PROJECTS & COMPETITIONS")
        projects = input("List projects/competitions (comma-separated): ").split(',')
        inputs['projects_competitions'] = [p.strip() for p in projects if p.strip()]
        
        print("\n4️⃣ HOBBIES")
        inputs['hobbies'] = input("What do you do in free time?: ")
        
        self.display_psychometric_resources("Stage 1")
        inputs['psychometric_results'] = self.collect_psychometric_results("Stage 1")
        
        return inputs
    
    def generate_stage1_output(self, name: str, grade: int, inputs: Dict) -> Dict:
        """Generate Stage 1 outputs"""
        output = {
            'stage': 'Stage 1: Exploration Years',
            'student_name': name,
            'grade': grade,
            'exploration_report': {},
            'suggested_pathways': [],
            'awareness_insights': [],
            'clubs_workshops': []
        }
        
        psychometric = inputs.get('psychometric_results', {})
        
        report = {
            'subject_inclinations': inputs['subject_preferences'],
            'creative_interests': inputs['extracurricular_activities'],
            'achievements': inputs['projects_competitions'],
            'personality_insights': {
                'type': psychometric.get('personality_type', 'Not assessed'),
                'strengths': self._extract_strengths_from_psychometric(psychometric, 'stage1')
            }
        }
        output['exploration_report'] = report
        
        pathways = []
        
        if any('Science' in s or 'Math' in s for s in inputs['subject_preferences']):
            pathways.extend(['Science Clubs', 'Math Olympiad', 'STEM Workshops'])
        
        if any('Coding' in a or 'Computer' in str(inputs['subject_preferences']) for a in inputs['extracurricular_activities']):
            pathways.extend(['Coding Bootcamps', 'Robotics Clubs', 'App Development'])
        
        if any('Arts' in a or 'Music' in a for a in inputs['extracurricular_activities']):
            pathways.extend(['Art Exhibitions', 'Music Competitions', 'Theatre Workshops'])
        
        output['suggested_pathways'] = list(set(pathways))
        
        interest_areas = psychometric.get('interest_areas', [])
        awareness = []
        
        for interest in interest_areas:
            for domain, careers in self.career_database.items():
                if interest.lower() in domain.lower():
                    awareness.append(f"{domain}: {', '.join(careers[:3])}")
        
        output['awareness_insights'] = awareness if awareness else [f"Explore {', '.join(list(self.career_database.keys())[:5])}"]
        
        clubs = [f"{activity} Club" for activity in inputs['extracurricular_activities']]
        output['clubs_workshops'] = list(set(clubs))
        
        return output
    
    def _extract_strengths_from_psychometric(self, psychometric: Dict, stage: str) -> List[str]:
        """Extract strengths from psychometric"""
        strengths = []
        
        if stage == 'stage1':
            if psychometric.get('creativity', 0) > 7:
                strengths.append('Creativity')
            if psychometric.get('logical_thinking', 0) > 7:
                strengths.append('Logical Thinking')
            if psychometric.get('social_skills', 0) > 7:
                strengths.append('Social Skills')
            if psychometric.get('leadership', 0) > 7:
                strengths.append('Leadership')
            if psychometric.get('artistic', 0) > 70:
                strengths.append('Artistic Expression')
            if psychometric.get('investigative', 0) > 70:
                strengths.append('Scientific Inquiry')
        
        elif stage == 'stage2':
            if psychometric.get('logical_reasoning', 0) > 70:
                strengths.append('Logical Reasoning')
            if psychometric.get('numerical_ability', 0) > 70:
                strengths.append('Numerical Skills')
            if psychometric.get('verbal_ability', 0) > 70:
                strengths.append('Communication')
        
        elif stage == 'stage3':
            if psychometric.get('technical_aptitude', 0) > 70:
                strengths.append('Technical Skills')
            if psychometric.get('analytical_skills', 0) > 70:
                strengths.append('Analytical Thinking')
            if psychometric.get('leadership_score', 0) > 70:
                strengths.append('Leadership')
        
        return strengths if strengths else ['Well-rounded capabilities']
    
    # ==================== STAGE 2: DECISION YEARS ====================
    
    def collect_stage2_inputs(self) -> Dict:
        """Collect Stage 2 inputs"""
        print("\n" + "="*70)
        print("🎯 STAGE 2: DECISION YEARS (CLASSES 10-12)")
        print("="*70)
        
        inputs = {}
        
        print("\n1️⃣ ACADEMIC STREAM")
        inputs['stream'] = input("Your stream (Science PCM/PCB, Commerce, Arts): ").strip()
        
        print("\n2️⃣ ACADEMIC PERFORMANCE")
        inputs['class10_percentage'] = float(input("Class 10 Percentage: ") or 0)
        inputs['current_percentage'] = float(input("Current Percentage (if 11/12): ") or # CONTINUATION OF NaviRiti Career Prediction System
# This is Part 2 - append this after Part 1

        0)
        
        print("\n3️⃣ SUBJECT STRENGTHS")
        subjects = input("Subjects you excel in (comma-separated): ").split(',')
        inputs['strong_subjects'] = [s.strip() for s in subjects if s.strip()]
        
        print("\n4️⃣ CAREER INTERESTS")
        print("Domains: Technology, Medical, Engineering, Business, Creative, Arts, Social, Law, Science, Sports")
        interests = input("Your career interests (comma-separated): ").split(',')
        inputs['career_interests'] = [i.strip() for i in interests if i.strip()]
        
        print("\n5️⃣ COMPETITIVE EXAMS")
        exams = input("Exams preparing for (JEE, NEET, CA, CLAT, etc.): ").split(',')
        inputs['competitive_exams'] = [e.strip() for e in exams if e.strip()]
        
        print("\n6️⃣ EXTRACURRICULAR ACHIEVEMENTS")
        inputs['extracurricular_achievements'] = input("Major achievements: ").strip()
        
        self.display_psychometric_resources("Stage 2")
        inputs['psychometric_results'] = self.collect_psychometric_results("Stage 2")
        
        return inputs
    
    def generate_stage2_output(self, name: str, grade: int, inputs: Dict) -> Dict:
        """Generate Stage 2 outputs"""
        output = {
            'stage': 'Stage 2: Decision Years',
            'student_name': name,
            'grade': grade,
            'stream': inputs['stream'],
            'academic_profile': {},
            'career_recommendations': [],
            'exam_guidance': {},
            'skill_development': []
        }
        
        psychometric = inputs.get('psychometric_results', {})
        
        output['academic_profile'] = {
            'class10_percentage': inputs['class10_percentage'],
            'current_performance': inputs['current_percentage'],
            'strong_subjects': inputs['strong_subjects'],
            'academic_rating': self._calculate_academic_rating(inputs)
        }
        
        output['career_recommendations'] = self._predict_careers_stage2(inputs, psychometric)
        output['exam_guidance'] = self._generate_exam_guidance(inputs)
        output['skill_development'] = self._suggest_skills_stage2(inputs, psychometric)
        
        return output
    
    def _calculate_academic_rating(self, inputs: Dict) -> str:
        """Calculate academic rating"""
        avg = (inputs['class10_percentage'] + inputs['current_percentage']) / 2
        if avg >= 90:
            return "Excellent"
        elif avg >= 75:
            return "Good"
        elif avg >= 60:
            return "Average"
        else:
            return "Needs Improvement"
    
    def _predict_careers_stage2(self, inputs: Dict, psychometric: Dict) -> List[Dict]:
        """Predict careers for Stage 2"""
        careers = []
        stream = inputs['stream'].lower()
        
        if 'science' in stream:
            if 'pcm' in stream or 'math' in stream:
                careers.extend([
                    {'career': 'Software Engineer', 'match': 90, 'domain': 'Technology'},
                    {'career': 'Data Scientist', 'match': 85, 'domain': 'Technology'},
                    {'career': 'Mechanical Engineer', 'match': 80, 'domain': 'Engineering'}
                ])
            if 'pcb' in stream or 'bio' in stream:
                careers.extend([
                    {'career': 'Doctor (MBBS)', 'match': 95, 'domain': 'Medical'},
                    {'career': 'Biotechnologist', 'match': 85, 'domain': 'Science'},
                    {'career': 'Pharmacist', 'match': 80, 'domain': 'Medical'}
                ])
        
        elif 'commerce' in stream:
            careers.extend([
                {'career': 'Chartered Accountant', 'match': 90, 'domain': 'Business'},
                {'career': 'Financial Analyst', 'match': 85, 'domain': 'Business'},
                {'career': 'Investment Banker', 'match': 80, 'domain': 'Business'}
            ])
        
        elif 'arts' in stream or 'humanities' in stream:
            careers.extend([
                {'career': 'Lawyer', 'match': 88, 'domain': 'Law'},
                {'career': 'Psychologist', 'match': 85, 'domain': 'Social'},
                {'career': 'Journalist', 'match': 82, 'domain': 'Arts'}
            ])
        
        if psychometric.get('logical_reasoning', 0) > 80:
            careers.append({'career': 'Software Engineer', 'match': 92, 'domain': 'Technology'})
        
        if psychometric.get('numerical_ability', 0) > 80:
            careers.append({'career': 'Data Scientist', 'match': 90, 'domain': 'Technology'})
        
        unique_careers = {c['career']: c for c in careers}
        return sorted(unique_careers.values(), key=lambda x: x['match'], reverse=True)[:8]
    
    def _generate_exam_guidance(self, inputs: Dict) -> Dict:
        """Generate exam guidance"""
        guidance = {}
        
        for exam in inputs['competitive_exams']:
            exam_lower = exam.lower()
            if 'jee' in exam_lower:
                guidance['JEE'] = {
                    'preparation_time': '2 years intensive',
                    'key_subjects': ['Physics', 'Chemistry', 'Mathematics'],
                    'resources': ['Coaching', 'Online platforms', 'Mock tests']
                }
            elif 'neet' in exam_lower:
                guidance['NEET'] = {
                    'preparation_time': '2 years intensive',
                    'key_subjects': ['Physics', 'Chemistry', 'Biology'],
                    'resources': ['Medical coaching', 'NCERT', 'Previous papers']
                }
            elif 'ca' in exam_lower:
                guidance['CA'] = {
                    'preparation_time': '5 years total',
                    'key_subjects': ['Accounting', 'Taxation', 'Auditing'],
                    'resources': ['ICAI materials', 'Articleship']
                }
        
        return guidance
    
    def _suggest_skills_stage2(self, inputs: Dict, psychometric: Dict) -> List[str]:
        """Suggest skills for Stage 2"""
        skills = []
        
        for interest in inputs['career_interests']:
            interest_lower = interest.lower()
            if 'tech' in interest_lower:
                skills.extend(['Programming (Python/Java)', 'Web Development', 'Data Structures'])
            if 'business' in interest_lower:
                skills.extend(['Excel Advanced', 'Financial Analysis', 'Communication'])
            if 'creative' in interest_lower:
                skills.extend(['Adobe Suite', 'Video Editing', 'Digital Marketing'])
        
        if psychometric.get('communication', 0) > 70:
            skills.append('Public Speaking')
        if psychometric.get('analytical_skills', 0) > 70:
            skills.append('Critical Thinking')
        
        return list(set(skills))[:10]
    
    # ==================== STAGE 3: UNDERGRADUATE ====================
    
    def collect_stage3_inputs(self) -> Dict:
        """Collect Stage 3 inputs"""
        print("\n" + "="*70)
        print("🎓 STAGE 3: UNDERGRADUATE CAREER PREDICTION")
        print("="*70)
        
        inputs = {}
        
        print("\n1️⃣ CV/RESUME UPLOAD (PDF)")
        cv_path = input("Enter CV PDF path (or press Enter to skip): ").strip()
        
        if cv_path and os.path.exists(cv_path):
            cv_data = self.parse_cv_pdf(cv_path)
            inputs['cv_data'] = cv_data
            inputs['has_cv'] = True
            
            if cv_data['parsed_successfully']:
                print(f"\n✅ AUTO-FILLED FROM CV:")
                print(f"   Name: {cv_data['name']}")
                print(f"   Email: {cv_data['email']}")
                print(f"   Skills: {len(cv_data['skills'])} detected")
        else:
            inputs['has_cv'] = False
            inputs['cv_data'] = {}
        
        print("\n2️⃣ ACADEMIC DETAILS")
        inputs['current_degree'] = input("Degree (e.g., B.Tech CSE, B.Com): ").strip()
        inputs['university'] = input("University/College: ").strip()
        inputs['current_year'] = int(input("Current Year (1/2/3/4): ") or 1)
        inputs['cgpa'] = float(input("Current CGPA/Percentage: ") or 0)
        
        print("\n3️⃣ TECHNICAL SKILLS")
        if not inputs['cv_data'].get('skills'):
            skills = input("List technical skills (comma-separated): ").split(',')
            inputs['technical_skills'] = [s.strip() for s in skills if s.strip()]
        else:
            inputs['technical_skills'] = inputs['cv_data']['skills']
            print(f"   Skills from CV: {', '.join(inputs['technical_skills'][:5])}...")
        
        print("\n4️⃣ INTERNSHIPS & EXPERIENCE")
        if not inputs['cv_data'].get('experience'):
            exp = input("Describe experience: ").strip()
            inputs['experience'] = [exp] if exp else []
        else:
            inputs['experience'] = inputs['cv_data']['experience']
            print(f"   {len(inputs['experience'])} entries from CV")
        
        print("\n5️⃣ PROJECTS")
        if not inputs['cv_data'].get('projects'):
            projects = input("List projects (comma-separated): ").split(',')
            inputs['projects'] = [p.strip() for p in projects if p.strip()]
        else:
            inputs['projects'] = inputs['cv_data']['projects']
            print(f"   {len(inputs['projects'])} projects from CV")
        
        print("\n6️⃣ CERTIFICATIONS")
        if not inputs['cv_data'].get('certifications'):
            certs = input("List certifications (comma-separated): ").split(',')
            inputs['certifications'] = [c.strip() for c in certs if c.strip()]
        else:
            inputs['certifications'] = inputs['cv_data']['certifications']
            print(f"   {len(inputs['certifications'])} certifications from CV")
        
        print("\n7️⃣ CAREER PREFERENCES")
        inputs['preferred_roles'] = input("Preferred job roles (comma-separated): ").split(',')
        inputs['preferred_roles'] = [r.strip() for r in inputs['preferred_roles'] if r.strip()]
        
        inputs['preferred_industries'] = input("Preferred industries (comma-separated): ").split(',')
        inputs['preferred_industries'] = [i.strip() for i in inputs['preferred_industries'] if i.strip()]
        
        self.display_psychometric_resources("Stage 3")
        inputs['psychometric_results'] = self.collect_psychometric_results("Stage 3")
        
        return inputs
    
    def generate_stage3_output(self, name: str, inputs: Dict) -> Dict:
        """Generate Stage 3 outputs"""
        output = {
            'stage': 'Stage 3: Undergraduate',
            'student_name': name,
            'degree': inputs['current_degree'],
            'employability_score': 0,
            'career_predictions': [],
            'job_role_mapping': [],
            'skill_gap_analysis': {},
            'industry_recommendations': [],
            'preparation_roadmap': {}
        }
        
        cv_data = inputs.get('cv_data', {})
        psychometric = inputs.get('psychometric_results', {})
        
        output['employability_score'] = self._calculate_employability_score(inputs, cv_data, psychometric)
        output['career_predictions'] = self._predict_careers_stage3(inputs, cv_data, psychometric)
        output['job_role_mapping'] = self._map_job_roles(inputs, cv_data)
        output['skill_gap_analysis'] = self._analyze_skill_gaps(inputs, output['career_predictions'])
        output['industry_recommendations'] = self._recommend_industries(inputs, psychometric)
        output['preparation_roadmap'] = self._create_preparation_roadmap(inputs, output)
        
        return output
    
    def _calculate_employability_score(self, inputs: Dict, cv_data: Dict, psychometric: Dict) -> int:
        """Calculate employability score"""
        score = 0
        
        cgpa = inputs.get('cgpa', 0)
        if cgpa >= 9.0:
            score += 25
        elif cgpa >= 8.0:
            score += 20
        elif cgpa >= 7.0:
            score += 15
        elif cgpa >= 6.0:
            score += 10
        
        skills_count = len(inputs.get('technical_skills', []))
        score += min(skills_count * 3, 25)
        
        exp_count = len(inputs.get('experience', []))
        score += min(exp_count * 10, 20)
        
        project_count = len(inputs.get('projects', []))
        score += min(project_count * 5, 15)
        
        cert_count = len(inputs.get('certifications', []))
        score += min(cert_count * 3, 10)
        
        if psychometric:
            avg_psychometric = sum([
                psychometric.get('technical_aptitude', 0),
                psychometric.get('communication', 0),
                psychometric.get('analytical_skills', 0)
            ]) / 3
            if avg_psychometric > 80:
                score += 5
        
        return min(score, 100)
    
    def _predict_careers_stage3(self, inputs: Dict, cv_data: Dict, psychometric: Dict) -> List[Dict]:
        """Predict careers for Stage 3"""
        careers = []
        degree = inputs['current_degree'].lower()
        skills = inputs.get('technical_skills', [])
        
        if 'computer' in degree or 'cse' in degree or 'it' in degree:
            careers.extend([
                {'career': 'Software Engineer', 'match': 95, 'salary_range': '₹6-15 LPA'},
                {'career': 'Data Scientist', 'match': 90, 'salary_range': '₹8-20 LPA'},
                {'career': 'Full Stack Developer', 'match': 88, 'salary_range': '₹5-12 LPA'},
                {'career': 'AI/ML Engineer', 'match': 85, 'salary_range': '₹10-25 LPA'}
            ])
        
        elif 'mechanical' in degree or 'civil' in degree:
            careers.extend([
                {'career': 'Mechanical Engineer', 'match': 90, 'salary_range': '₹4-10 LPA'},
                {'career': 'Design Engineer', 'match': 85, 'salary_range': '₹5-12 LPA'}
            ])
        
        elif 'commerce' in degree or 'bcom' in degree:
            careers.extend([
                {'career': 'Financial Analyst', 'match': 88, 'salary_range': '₹4-10 LPA'},
                {'career': 'Accountant', 'match': 85, 'salary_range': '₹3-8 LPA'}
            ])
        
        elif 'mba' in degree:
            careers.extend([
                {'career': 'Product Manager', 'match': 92, 'salary_range': '₹10-25 LPA'},
                {'career': 'Management Consultant', 'match': 90, 'salary_range': '₹12-30 LPA'}
            ])
        
        skill_str = ' '.join(skills).lower()
        if 'python' in skill_str or 'java' in skill_str:
            careers.append({'career': 'Backend Developer', 'match': 90, 'salary_range': '₹6-14 LPA'})
        
        if 'react' in skill_str or 'angular' in skill_str:
            careers.append({'career': 'Frontend Developer', 'match': 88, 'salary_range': '₹5-12 LPA'})
        
        if psychometric.get('leadership_score', 0) > 80:
            careers.append({'career': 'Team Lead', 'match': 85, 'salary_range': '₹12-25 LPA'})
        
        unique_careers = {c['career']: c for c in careers}
        return sorted(unique_careers.values(), key=lambda x: x['match'], reverse=True)[:10]
    
    def _map_job_roles(self, inputs: Dict, cv_data: Dict) -> List[Dict]:
        """Map job roles"""
        job_roles = []
        skills = inputs.get('technical_skills', [])
        skill_str = ' '.join(skills).lower()
        
        if any(skill in skill_str for skill in ['python', 'java', 'javascript']):
            job_roles.append({
                'role': 'Software Development Engineer',
                'companies': ['Google', 'Microsoft', 'Amazon', 'Adobe'],
                'required_skills': ['DSA', 'OOP', 'System Design'],
                'readiness': 'High' if len(skills) >= 5 else 'Medium'
            })
        
        if 'data' in skill_str or 'sql' in skill_str:
            job_roles.append({
                'role': 'Data Analyst',
                'companies': ['Deloitte', 'EY', 'McKinsey'],
                'required_skills': ['SQL', 'Excel', 'Tableau', 'Python'],
                'readiness': 'Medium'
            })
        
        return job_roles[:8]
    
    def _analyze_skill_gaps(self, inputs: Dict, career_predictions: List[Dict]) -> Dict:
        """Analyze skill gaps"""
        current_skills = set(skill.lower() for skill in inputs.get('technical_skills', []))
        gaps = {}
        
        for career in career_predictions[:3]:
            career_name = career['career']
            required_skills = self.skill_requirements.get(career_name, [])
            
            missing_skills = [skill for skill in required_skills 
                            if skill.lower() not in current_skills]
            
            gaps[career_name] = {
                'missing_skills': missing_skills,
                'completion_percentage': int((1 - len(missing_skills)/len(required_skills)) * 100) if required_skills else 0,
                'learning_resources': self._get_learning_resources(missing_skills)
            }
        
        return gaps
    
    def _get_learning_resources(self, skills: List[str]) -> List[str]:
        """Get learning resources"""
        resources = []
        for skill in skills[:3]:
            skill_lower = skill.lower()
            if 'python' in skill_lower:
                resources.append('Coursera: Python for Everybody')
            elif 'java' in skill_lower:
                resources.append('Udemy: Complete Java Masterclass')
            elif 'machine learning' in skill_lower:
                resources.append('Coursera: ML by Andrew Ng')
            else:
                resources.append(f'{skill} tutorials online')
        
        return resources
    
    def _recommend_industries(self, inputs: Dict, psychometric: Dict) -> List[Dict]:
        """Recommend industries"""
        industries = []
        degree = inputs['current_degree'].lower()
        
        if 'computer' in degree or 'tech' in degree:
            industries.extend([
                {'industry': 'IT Services', 'growth': 'High', 'avg_salary': '₹6-12 LPA'},
                {'industry': 'Product Companies', 'growth': 'Very High', 'avg_salary': '₹10-25 LPA'}
            ])
        
        if 'mechanical' in degree:
            industries.extend([
                {'industry': 'Manufacturing', 'growth': 'Medium', 'avg_salary': '₹4-10 LPA'}
            ])
        
        return industries[:8]
    
    def _create_preparation_roadmap(self, inputs: Dict, output: Dict) -> Dict:
        """Create preparation roadmap"""
        year = inputs.get('current_year', 1)
        
        roadmap = {
            'immediate_actions': [],
            'short_term_goals': [],
            'long_term_goals': []
        }
        
        if output['employability_score'] < 60:
            roadmap['immediate_actions'].append('Build core technical skills')
        
        if len(inputs.get('projects', [])) < 2:
            roadmap['immediate_actions'].append('Start 2-3 significant projects')
        
        if not inputs.get('experience'):
            roadmap['immediate_actions'].append('Apply for internships')
        
        roadmap['short_term_goals'].append('Build portfolio website')
        roadmap['short_term_goals'].append('Network on LinkedIn')
        
        if year <= 2:
            roadmap['long_term_goals'].append('Complete 2 internships before graduation')
        
        roadmap['long_term_goals'].append('Prepare for campus placements')
        
        return roadmap
    
    # ==================== REPORT GENERATION ====================
    
    def print_stage1_report(self, output: Dict):
        """Print Stage 1 report"""
        print("\n" + "="*80)
        print("📊 NAVIRITI CAREER EXPLORATION REPORT - STAGE 1")
        print("="*80)
        print(f"Student: {output['student_name']}")
        print(f"Grade: {output['grade']}")
        print("="*80)
        
        report = output['exploration_report']
        print("\n📚 SUBJECT INCLINATIONS:")
        for subject in report['subject_inclinations']:
            print(f"   • {subject}")
        
        print("\n🎨 CREATIVE INTERESTS:")
        for interest in report['creative_interests']:
            print(f"   • {interest}")
        
        print("\n👤 PERSONALITY INSIGHTS:")
        print(f"   Type: {report['personality_insights']['type']}")
        print("   Strengths:", ", ".join(report['personality_insights']['strengths']))
        
        print("\n🛤️  SUGGESTED PATHWAYS:")
        for pathway in output['suggested_pathways']:
            print(f"   • {pathway}")
        
        print("\n" + "="*80)
    
    def print_stage2_report(self, output: Dict):
        """Print Stage 2 report"""
        print("\n" + "="*80)
        print("📊 NAVIRITI CAREER PREDICTION REPORT - STAGE 2")
        print("="*80)
        print(f"Student: {output['student_name']}")
        print(f"Grade: {output['grade']}")
        print(f"Stream: {output['stream']}")
        print("="*80)
        
        print("\n📚 ACADEMIC PROFILE:")
        prof = output['academic_profile']
        print(f"   Class 10: {prof['class10_percentage']}%")
        print(f"   Current: {prof['current_percentage']}%")
        print(f"   Rating: {prof['academic_rating']}")
        
        print("\n🎯 CAREER RECOMMENDATIONS:")
        for career in output['career_recommendations'][:5]:
            print(f"   • {career['career']} - Match: {career['match']}% ({career['domain']})")
        
        print("\n📖 EXAM GUIDANCE:")
        for exam, guide in output['exam_guidance'].items():
            print(f"\n   {exam}:")
            print(f"      Time: {guide['preparation_time']}")
            print(f"      Subjects: {', '.join(guide['key_subjects'])}")
        
        print("\n" + "="*80)
    
    def print_stage3_report(self, output: Dict):
        """Print Stage 3 report"""
        print("\n" + "="*80)
        print("📊 NAVIRITI CAREER PREDICTION REPORT - STAGE 3")
        print("="*80)
        print(f"Student: {output['student_name']}")
        print(f"Degree: {output['degree']}")
        print(f"Employability Score: {output['employability_score']}/100")
        print("="*80)
        
        print("\n🎯 TOP CAREER PREDICTIONS:")
        for career in output['career_predictions'][:5]:
            print(f"   • {career['career']} - Match: {career['match']}%")
            print(f"     Salary: {career['salary_range']}")
        
        print("\n💼 JOB ROLE MAPPING:")
        for job in output['job_role_mapping'][:3]:
            print(f"\n   {job['role']}:")
            print(f"      Companies: {', '.join(job['companies'][:3])}")
            print(f"      Readiness: {job['readiness']}")
        
        print("\n📊 SKILL GAP ANALYSIS:")
        for career, gap in list(output['skill_gap_analysis'].items())[:2]:
            print(f"\n   {career}:")
            print(f"      Completion: {gap['completion_percentage']}%")
            print(f"      Missing: {', '.join(gap['missing_skills'][:3])}")
        
        print("\n🗺️ PREPARATION ROADMAP:")
        print("\n   Immediate Actions:")
        for action in output['preparation_roadmap']['immediate_actions']:
            print(f"      • {action}")
        
        print("\n   Short-term Goals (3-6 months):")
        for goal in output['preparation_roadmap']['short_term_goals']:
            print(f"      • {goal}")
        
        print("\n" + "="*80)
    
    def save_report(self, output: Dict, filename: str = None):
        """Save report to JSON"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"naviriti_report_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"\n✅ Report saved to: {filename}")
    
    # ==================== MAIN EXECUTION ====================
    
    def run(self):
        """Main execution function"""
        print("\n" + "="*80)
        print("🌟 WELCOME TO NAVIRITI CAREER PREDICTION SYSTEM 🌟")
        print("="*80)
        print("Your personalized AI-powered career guidance platform")
        print("="*80)
        
        name = input("\nEnter your name: ").strip()
        grade = int(input("Enter your current grade/year: ") or 0)
        
        stage = self.get_student_stage(grade)
        print(f"\n📍 Identified Stage: {stage}")
        
        if "Stage 1" in stage:
            inputs = self.collect_stage1_inputs()
            output = self.generate_stage1_output(name, grade, inputs)
            self.print_stage1_report(output)
            
        elif "Stage 2" in stage:
            inputs = self.collect_stage2_inputs()
            output = self.generate_stage2_output(name, grade, inputs)
            self.print_stage2_report(output)
            
        elif "Stage 3" in stage:
            inputs = self.collect_stage3_inputs()
            output = self.generate_stage3_output(name, inputs)
            self.print_stage3_report(output)
        
        else:
            print("\n❌ Invalid grade/year entered!")
            return
        
        save = input("\nSave report? (yes/no): ").lower()
        if save == 'yes':
            self.save_report(output)
        
        print("\n✅ Thank you for using NaviRiti! Good luck with your career journey! 🚀")


# ==================== RUN THE SYSTEM ====================

if __name__ == "__main__":
    predictor = NaviRitiCareerPredictor()
    predictor.run()