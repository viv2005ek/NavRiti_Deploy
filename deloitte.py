import json
from datetime import datetime
from typing import Dict, List, Any
import os

class NaviRitiCareerPredictor:
    """
    NaviRiti Career Prediction System - Phase 1 (Release 1.0)
    Complete Student-Centric Approach with All SRS Inputs
    """
    
    def __init__(self):
        self.career_database = self._initialize_career_database()
        self.skill_requirements = self._initialize_skill_requirements()
        
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
            'Teacher': ['Subject Knowledge', 'Communication', 'Patience', 'Creativity', 'Leadership']
        }
    
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
    
    # ==================== STAGE 1: EXPLORATION YEARS (6-9) ====================
    
    def collect_stage1_inputs(self) -> Dict:
        """Collect all inputs for Stage 1: Exploration Years"""
        print("\n" + "="*70)
        print("📚 STAGE 1: EXPLORATION YEARS (CLASSES 6-9)")
        print("="*70)
        
        inputs = {}
        
        # 1. Subject Preferences
        print("\n1️⃣ SUBJECT PREFERENCES")
        print("Available subjects: Mathematics, Science, English, Social Studies,")
        print("                   Computer Science, Arts, Languages, Physical Education")
        subjects = input("Enter subjects you enjoy most (comma-separated): ").split(',')
        inputs['subject_preferences'] = [s.strip() for s in subjects if s.strip()]
        
        # 2. Extracurricular Activities
        print("\n2️⃣ EXTRACURRICULAR ACTIVITIES")
        print("Options: Sports, Arts, Music, Drama, Coding, Debates, Dance, Robotics,")
        print("         Photography, Writing, Public Speaking")
        activities = input("Enter your extracurricular activities (comma-separated): ").split(',')
        inputs['extracurricular_activities'] = [a.strip() for a in activities if a.strip()]
        
        # 3. Projects & Competitions
        print("\n3️⃣ PROJECTS & COMPETITIONS")
        print("Examples: Science fairs, Essay contests, Coding challenges, Art exhibitions,")
        print("          Math olympiads, Debate competitions")
        projects = input("List any projects/competitions participated (comma-separated): ").split(',')
        inputs['projects_competitions'] = [p.strip() for p in projects if p.strip()]
        
        # 4. Hobbies and Interests
        print("\n4️⃣ HOBBIES & CREATIVE INTERESTS")
        hobbies = input("What do you do in your free time? (describe briefly): ")
        inputs['hobbies'] = hobbies
        
        # 5. Psychometric Test Results (External)
        print("\n5️⃣ PSYCHOMETRIC TEST RESULTS")
        print("Enter results from external psychometric assessment:")
        
        print("\nPersonality Type (e.g., Creative, Analytical, Social, Practical): ")
        inputs['personality_type'] = input("Type: ").strip()
        
        print("\nStrong Traits (e.g., Leadership, Creativity, Logic, Empathy):")
        traits = input("Traits (comma-separated): ").split(',')
        inputs['strong_traits'] = [t.strip() for t in traits if t.strip()]
        
        print("\nInterest Areas from test (e.g., Technology, Arts, Science, Sports):")
        interests = input("Interest areas (comma-separated): ").split(',')
        inputs['psychometric_interests'] = [i.strip() for i in interests if i.strip()]
        
        return inputs
    
    def generate_stage1_output(self, name: str, grade: int, inputs: Dict) -> Dict:
        """Generate outputs for Stage 1: Exploration Report"""
        output = {
            'stage': 'Stage 1: Exploration Years',
            'student_name': name,
            'grade': grade,
            'exploration_report': {},
            'suggested_pathways': [],
            'awareness_insights': [],
            'clubs_workshops': []
        }
        
        # Analyze inputs to create exploration report
        report = {
            'subject_inclinations': inputs['subject_preferences'],
            'creative_interests': inputs['extracurricular_activities'],
            'achievements': inputs['projects_competitions'],
            'personality_insights': {
                'type': inputs['personality_type'],
                'strengths': inputs['strong_traits']
            }
        }
        output['exploration_report'] = report
        
        # Suggest pathways based on interests
        pathways = []
        
        if any('Science' in s or 'Math' in s for s in inputs['subject_preferences']):
            pathways.extend(['Science Clubs', 'Math Olympiad Preparation', 'STEM Workshops'])
        
        if any('Coding' in a or 'Computer' in str(inputs['subject_preferences']) for a in inputs['extracurricular_activities']):
            pathways.extend(['Coding Bootcamps', 'Robotics Clubs', 'App Development Workshops'])
        
        if any('Arts' in a or 'Music' in a or 'Drama' in a for a in inputs['extracurricular_activities']):
            pathways.extend(['Art Exhibitions', 'Music Competitions', 'Theatre Workshops'])
        
        if any('Sports' in a for a in inputs['extracurricular_activities']):
            pathways.extend(['Sports Academies', 'Fitness Programs', 'Sports Leadership Camps'])
        
        output['suggested_pathways'] = pathways
        
        # Career awareness (NOT predictions, just exposure)
        awareness = []
        for interest in inputs['psychometric_interests']:
            if interest in self.career_database:
                awareness.append(f"{interest} Domain: Explore fields like {', '.join(self.career_database[interest][:3])}")
        
        output['awareness_insights'] = awareness
        
        # Recommend clubs and workshops
        clubs = []
        for activity in inputs['extracurricular_activities']:
            clubs.append(f"{activity} Club/Workshop")
        
        output['clubs_workshops'] = list(set(clubs))
        
        return output
    
    # ==================== STAGE 2: DECISION YEARS (10-12) ====================
    
    def collect_stage2_inputs(self) -> Dict:
        """Collect all inputs for Stage 2: Decision Years"""
        print("\n" + "="*70)
        print("🎓 STAGE 2: DECISION YEARS (CLASSES 10-12)")
        print("="*70)
        
        inputs = {}
        
        # 1. Stream Choice
        print("\n1️⃣ STREAM CHOICE & ACADEMIC RECORDS")
        print("Available streams: PCM (Science with Math), PCB (Science with Biology),")
        print("                   PCMB (All Sciences), Commerce, Arts/Humanities")
        inputs['stream_choice'] = input("Current/Preferred stream: ").strip()
        
        # 2. Academic Performance
        print("\nAcademic Performance (Class 9/10 or current marks):")
        subjects = []
        if 'PCM' in inputs['stream_choice'] or 'PCB' in inputs['stream_choice']:
            subjects = ['Physics', 'Chemistry', 'Mathematics/Biology']
        elif 'Commerce' in inputs['stream_choice']:
            subjects = ['Accountancy', 'Business Studies', 'Economics']
        elif 'Arts' in inputs['stream_choice']:
            subjects = ['History', 'Political Science', 'English']
        else:
            subjects = ['Subject 1', 'Subject 2', 'Subject 3']
        
        performance = {}
        for subject in subjects:
            marks = input(f"  {subject} (out of 100): ")
            if marks:
                performance[subject] = float(marks)
        inputs['academic_performance'] = performance
        
        # 3. Subject Preferences (within stream)
        print("\nWhich subjects do you enjoy most in your stream?")
        pref_subjects = input("Subjects (comma-separated): ").split(',')
        inputs['subject_preferences'] = [s.strip() for s in pref_subjects if s.strip()]
        
        # 4. Real-world exposure
        print("\n2️⃣ REAL-WORLD EXPOSURE")
        
        print("\nHave you done any internships/shadowing?")
        internships = input("List any (comma-separated, or press Enter if none): ").split(',')
        inputs['internships'] = [i.strip() for i in internships if i.strip()]
        
        print("\nClubs/Volunteering activities:")
        clubs = input("Activities (comma-separated): ").split(',')
        inputs['clubs_volunteering'] = [c.strip() for c in clubs if c.strip()]
        
        # 5. Projects and Portfolio
        print("\n3️⃣ INDEPENDENT PROJECTS & PORTFOLIO")
        print("Any projects you've built? (websites, research papers, art portfolio, etc.)")
        projects = input("Describe projects (comma-separated): ").split(',')
        inputs['independent_projects'] = [p.strip() for p in projects if p.strip()]
        
        # 6. Psychometric Test Results (Advanced for 10-12)
        print("\n4️⃣ PSYCHOMETRIC TEST RESULTS (Advanced)")
        
        print("\nAptitude Scores:")
        print("  Logical Reasoning (0-100):")
        inputs['logical_reasoning'] = float(input("  Score: ") or 0)
        
        print("  Verbal Ability (0-100):")
        inputs['verbal_ability'] = float(input("  Score: ") or 0)
        
        print("  Numerical Ability (0-100):")
        inputs['numerical_ability'] = float(input("  Score: ") or 0)
        
        print("\nCareer Interest Areas from test:")
        interests = input("Areas (comma-separated): ").split(',')
        inputs['career_interests'] = [i.strip() for i in interests if i.strip()]
        
        print("\nPersonality Type:")
        inputs['personality_type'] = input("Type: ").strip()
        
        # 7. Family and Societal Expectations
        print("\n5️⃣ FAMILY & SOCIETAL EXPECTATIONS")
        print("What career fields do your family prefer? (be honest)")
        family_pref = input("Family preferences (comma-separated): ").split(',')
        inputs['family_expectations'] = [f.strip() for f in family_pref if f.strip()]
        
        print("\nAre there any societal/cultural influences on your career choice?")
        inputs['societal_influences'] = input("Describe briefly: ").strip()
        
        return inputs
    
    def generate_stage2_output(self, name: str, grade: int, inputs: Dict) -> Dict:
        """Generate outputs for Stage 2: Career Predictions & Roadmap"""
        output = {
            'stage': 'Stage 2: Decision Years',
            'student_name': name,
            'grade': grade,
            'stream': inputs['stream_choice'],
            'predicted_careers': [],
            'alternate_careers': [],
            'career_roadmap': {},
            'competitive_exams': [],
            'skills_to_develop': [],
            'internship_recommendations': [],
            'higher_education_paths': []
        }
        
        # Career prediction based on stream and aptitudes
        stream = inputs['stream_choice'].upper()
        
        if 'PCM' in stream:
            careers = ['Software Engineer', 'Data Scientist', 'Mechanical Engineer', 
                      'Civil Engineer', 'Aerospace Engineer', 'Architect']
            exams = ['JEE Main', 'JEE Advanced', 'BITSAT', 'VITEEE', 'NATA (Architecture)']
        elif 'PCB' in stream:
            careers = ['Doctor (MBBS)', 'Dentist (BDS)', 'Pharmacist', 'Biotechnologist',
                      'Physiotherapist', 'Medical Research']
            exams = ['NEET', 'AIIMS', 'JIPMER', 'State Medical Exams']
        elif 'COMMERCE' in stream:
            careers = ['Chartered Accountant', 'Investment Banker', 'Financial Analyst',
                      'Business Analyst', 'Entrepreneur', 'Economist']
            exams = ['CA Foundation', 'CS Foundation', 'CLAT', 'IPMAT', 'CUET']
        elif 'ARTS' in stream or 'HUMANITIES' in stream:
            careers = ['Lawyer', 'Civil Servant (IAS/IPS)', 'Journalist', 'Psychologist',
                      'Social Worker', 'Content Creator', 'Teacher']
            exams = ['CLAT', 'UPSC CSE', 'CUET', 'JMI Entrance', 'DU JAT']
        else:
            careers = ['Explore multiple paths based on interests']
            exams = []
        
        # Refine based on psychometric results
        if inputs['logical_reasoning'] > 70:
            careers = [c for c in careers if 'Engineer' in c or 'Analyst' in c or 'Scientist' in c] + careers
        
        if inputs['verbal_ability'] > 70:
            if 'Lawyer' not in careers:
                careers.append('Lawyer')
            if 'Journalist' not in careers:
                careers.append('Journalist')
        
        # Consider family expectations
        for family_choice in inputs['family_expectations']:
            for domain, domain_careers in self.career_database.items():
                if family_choice.lower() in domain.lower():
                    careers.extend(domain_careers[:2])
        
        # Remove duplicates and limit
        output['predicted_careers'] = list(dict.fromkeys(careers))[:5]
        output['alternate_careers'] = list(dict.fromkeys(careers))[5:8]
        
        output['competitive_exams'] = exams
        
        # Generate detailed roadmap for top career
        if output['predicted_careers']:
            top_career = output['predicted_careers'][0]
            output['career_roadmap'] = self._generate_detailed_roadmap(top_career, inputs['stream_choice'])
        
        # Skills to develop
        if output['predicted_careers']:
            career = output['predicted_careers'][0]
            if career in self.skill_requirements:
                output['skills_to_develop'] = self.skill_requirements[career]
        
        # Internship recommendations
        output['internship_recommendations'] = [
            f"Look for internships in {output['predicted_careers'][0]} domain",
            "Connect with professionals on LinkedIn",
            "Join relevant college clubs and societies",
            "Attend industry webinars and workshops"
        ]
        
        # Higher education paths
        if 'Engineer' in str(output['predicted_careers']):
            output['higher_education_paths'] = ['B.Tech/B.E.', 'B.Arch', 'Integrated M.Tech']
        elif 'Doctor' in str(output['predicted_careers']):
            output['higher_education_paths'] = ['MBBS', 'BDS', 'BAMS', 'BHMS']
        elif 'CA' in str(output['predicted_careers']) or 'Commerce' in stream:
            output['higher_education_paths'] = ['B.Com + CA', 'BBA', 'B.Com + CS', 'BMS']
        else:
            output['higher_education_paths'] = ['BA/BSc', 'BBA', 'LLB', 'Integrated Programs']
        
        return output
    
    # ==================== STAGE 3: UNDERGRADUATE ====================
    
    def collect_stage3_inputs(self) -> Dict:
        """Collect all inputs for Stage 3: Undergraduate"""
        print("\n" + "="*70)
        print("🎯 STAGE 3: UNDERGRADUATE STAGE")
        print("="*70)
        
        inputs = {}
        
        # 1. Academic Reports
        print("\n1️⃣ ACADEMIC PERFORMANCE")
        inputs['current_degree'] = input("Current Degree (e.g., B.Tech CSE, B.Com, BA Psychology): ").strip()
        inputs['current_year'] = input("Current Year (1/2/3/4): ").strip()
        
        print("\nCurrent CGPA/Percentage:")
        inputs['cgpa'] = float(input("CGPA (out of 10) or % (out of 100): ") or 0)
        
        print("\nSemester-wise performance trend:")
        trend = input("Trend (Improving/Stable/Declining): ").strip()
        inputs['academic_trend'] = trend
        
        # 2. Document Ingestion (Simulated - in real system, parse PDFs)
        print("\n2️⃣ PROFESSIONAL DOCUMENTS")
        print("Do you have the following? (we'll note them for analysis)")
        
        has_cv = input("Do you have a CV/Resume? (yes/no): ").lower() == 'yes'
        inputs['has_cv'] = has_cv
        
        if has_cv:
            print("\nKey highlights from your CV:")
            inputs['cv_highlights'] = input("Summary: ").strip()
        
        print("\nIndustry-specific certifications (comma-separated):")
        certs = input("Certifications: ").split(',')
        inputs['certifications'] = [c.strip() for c in certs if c.strip()]
        
        # 3. Internships & Research
        print("\n3️⃣ INTERNSHIPS & RESEARCH EXPERIENCE")
        
        print("\nNumber of internships completed:")
        num_internships = int(input("Count: ") or 0)
        
        internships = []
        for i in range(num_internships):
            print(f"\nInternship {i+1}:")
            company = input("  Company/Organization: ").strip()
            role = input("  Role: ").strip()
            duration = input("  Duration (months): ").strip()
            internships.append({
                'company': company,
                'role': role,
                'duration': duration
            })
        inputs['internships'] = internships
        
        print("\nAny research papers/publications?")
        research = input("List titles (comma-separated, or press Enter if none): ").split(',')
        inputs['research_publications'] = [r.strip() for r in research if r.strip()]
        
        # 4. Independent Passion Projects
        print("\n4️⃣ INDEPENDENT PROJECTS & INITIATIVES")
        
        print("\nPersonal projects (GitHub, portfolio, etc.):")
        projects = input("Describe projects (comma-separated): ").split(',')
        inputs['personal_projects'] = [p.strip() for p in projects if p.strip()]
        
        print("\nStartup/Entrepreneurial ventures:")
        startup = input("Any ventures? (yes/no): ").lower() == 'yes'
        if startup:
            inputs['startup_details'] = input("Describe briefly: ").strip()
        else:
            inputs['startup_details'] = None
        
        print("\nContent creation (blogs, YouTube, etc.):")
        content = input("Describe (or press Enter if none): ").strip()
        inputs['content_creation'] = content if content else None
        
        # 5. Skills Assessment
        print("\n5️⃣ SKILLS INVENTORY")
        
        print("\nTechnical Skills (comma-separated):")
        tech_skills = input("Skills: ").split(',')
        inputs['technical_skills'] = [s.strip() for s in tech_skills if s.strip()]
        
        print("\nSoft Skills (comma-separated):")
        soft_skills = input("Skills: ").split(',')
        inputs['soft_skills'] = [s.strip() for s in soft_skills if s.strip()]
        
        print("\nLanguages known:")
        languages = input("Languages (comma-separated): ").split(',')
        inputs['languages'] = [l.strip() for l in languages if l.strip()]
        
        # 6. Career Goals
        print("\n6️⃣ CAREER GOALS & PREFERENCES")
        
        print("\nPreferred career path:")
        inputs['preferred_career'] = input("Career: ").strip()
        
        print("\nJob vs Higher Studies preference:")
        inputs['job_vs_study'] = input("(Job/Higher Studies/Both/Undecided): ").strip()
        
        print("\nPreferred locations for work:")
        locations = input("Locations (comma-separated): ").split(',')
        inputs['preferred_locations'] = [l.strip() for l in locations if l.strip()]
        
        # 7. Psychometric Results (Professional Level)
        print("\n7️⃣ PSYCHOMETRIC ASSESSMENT (Professional)")
        
        print("\nCareer Aptitude Scores:")
        inputs['leadership_score'] = float(input("Leadership (0-100): ") or 0)
        inputs['technical_aptitude'] = float(input("Technical Aptitude (0-100): ") or 0)
        inputs['creative_thinking'] = float(input("Creative Thinking (0-100): ") or 0)
        inputs['analytical_skills'] = float(input("Analytical Skills (0-100): ") or 0)
        
        return inputs
    
    def generate_stage3_output(self, name: str, inputs: Dict) -> Dict:
        """Generate outputs for Stage 3: Career Mapping & Employability"""
        output = {
            'stage': 'Stage 3: Undergraduate',
            'student_name': name,
            'degree': inputs['current_degree'],
            'career_mapping': [],
            'employability_score': 0,
            'skill_gap_analysis': {},
            'graduate_pathways': {},
            'resume_enhancement': [],
            'job_readiness': {},
            'recommended_companies': [],
            'learning_resources': []
        }
        
        # Career mapping based on degree and skills
        degree = inputs['current_degree'].lower()
        careers = []
        
        if 'tech' in degree or 'computer' in degree or 'it' in degree:
            careers = ['Software Engineer', 'Data Scientist', 'Full Stack Developer', 
                      'DevOps Engineer', 'Product Manager']
        elif 'mech' in degree or 'civil' in degree or 'electrical' in degree:
            careers = ['Core Engineer', 'Project Manager', 'Consultant', 'R&D Engineer']
        elif 'commerce' in degree or 'bba' in degree or 'mba' in degree:
            careers = ['Financial Analyst', 'Business Analyst', 'Marketing Manager', 
                      'Consultant', 'Entrepreneur']
        elif 'arts' in degree or 'humanities' in degree:
            careers = ['Content Strategist', 'UX Researcher', 'Policy Analyst', 
                      'HR Manager', 'Counselor']
        else:
            careers = ['Explore based on skills and interests']
        
        # Refine based on skills and psychometric scores
        if inputs['technical_aptitude'] > 75:
            careers.insert(0, 'Technical Lead')
        if inputs['leadership_score'] > 75:
            careers.insert(0, 'Team Lead / Manager')
        if inputs['creative_thinking'] > 75:
            careers.insert(0, 'Product Designer / Creative Lead')
        
        output['career_mapping'] = list(dict.fromkeys(careers))[:6]
        
        # Calculate employability score
        score = 0
        if inputs['cgpa'] >= 7.5:
            score += 25
        elif inputs['cgpa'] >= 6.5:
            score += 15
        
        score += min(len(inputs['internships']) * 15, 30)
        score += min(len(inputs['certifications']) * 5, 15)
        score += min(len(inputs['personal_projects']) * 10, 20)
        
        if inputs['has_cv']:
            score += 10
        
        output['employability_score'] = min(score, 100)
        
        # Skill gap analysis
        if output['career_mapping']:
            target_career = inputs.get('preferred_career') or output['career_mapping'][0]
            required_skills = self.skill_requirements.get(target_career, 
                ['Domain Knowledge', 'Communication', 'Problem Solving'])
            
            current_skills = set(s.lower() for s in inputs['technical_skills'] + inputs['soft_skills'])
            required_skills_set = set(s.lower() for s in required_skills)
            
            output['skill_gap_analysis'] = {
                'target_career': target_career,
                'required_skills': required_skills,
                'skills_you_have': [s for s in required_skills if s.lower() in current_skills],
                'skills_to_develop': [s for s in required_skills if s.lower() not in current_skills],
                'additional_skills': list(current_skills - required_skills_set)
            }
        
        # Graduate pathways
        preference = inputs['job_vs_study']
        
        if 'job' in preference.lower():
            output['graduate_pathways'] = {
                'primary': 'Job Placement',
                'focus': 'Placement preparation, mock interviews, resume building',
                'timeline': 'Next 6 months',
                'actions': [
                    'Apply to companies via campus placement',
                    'Practice DSA/Technical skills',
                    'Build strong LinkedIn profile',
                    'Network with alumni'
                ]
            }
        elif 'higher' in preference.lower() or 'studies' in preference.lower():
            output['graduate_pathways'] = {
                'primary': 'Higher Studies (MS/MBA/MTech)',
                'focus': 'Entrance exam preparation, SOP writing, LORs',
                'timeline': 'Next 12-18 months',
                'actions': [
                    'Prepare for GRE/GMAT/GATE',
                    'Research universities/programs',
                    'Build research profile',
                    'Secure strong recommendations'
                ]
            }
        else:
            output['graduate_pathways'] = {
                'primary': 'Dual Track (Job + Higher Studies applications)',
                'focus': 'Keep both options open',
                'timeline': 'Next 6-12 months',
                'actions': [
                    'Apply for jobs',
                    'Simultaneously prepare for entrance exams',
                    'Build versatile profile'
                ]
            }
        
        # Resume enhancement
        enhancements = []
        
        if inputs['cgpa'] >= 7.0:
            enhancements.append(f"✓ Highlight strong CGPA ({inputs['cgpa']})")
        else:
            enhancements.append("• Focus on projects and skills over CGPA")
        
        if inputs['internships']:
            enhancements.append(f"✓ Emphasize {len(inputs['internships'])} internship(s) with quantifiable impact")
        else:
            enhancements.append("• URGENT: Complete at least 1-2 internships before graduation")
        
        if inputs['personal_projects']:
            enhancements.append(f"✓ Showcase {len(inputs['personal_projects'])} project(s) with GitHub/portfolio links")
        else:
            enhancements.append("• Build 2-3 strong projects to demonstrate practical skills")
        
        if inputs['certifications']:
            enhancements.append(f"✓ List {len(inputs['certifications'])} certification(s)")
        else:
            enhancements.append("• Consider industry-relevant certifications")
        
        if not inputs['has_cv']:
            enhancements.append("• CREATE A PROFESSIONAL CV/RESUME IMMEDIATELY")
        
        output['resume_enhancement'] = enhancements
        
        # Job readiness assessment
        output['job_readiness'] = {
            'overall_score': output['employability_score'],
            'technical_readiness': 'High' if len(inputs['technical_skills']) >= 5 else 'Medium' if len(inputs['technical_skills']) >= 3 else 'Low',
            'experience_level': 'Good' if len(inputs['internships']) >= 2 else 'Moderate' if len(inputs['internships']) >= 1 else 'Limited',
            'profile_strength': 'Strong' if inputs['has_cv'] and inputs['personal_projects'] else 'Needs Work',
            'immediate_actions': self._get_immediate_actions(inputs)
        }
        
        # Recommend companies/sectors
        if 'software' in degree.lower() or 'computer' in degree.lower():
            output['recommended_companies'] = ['Tech Giants (Google, Microsoft, Amazon)', 
                                              'Product Companies (Atlassian, Adobe)',
                                              'Startups', 'Service Companies (TCS, Infosys, Wipro)']
        elif 'commerce' in degree.lower() or 'finance' in degree.lower():
            output['recommended_companies'] = ['Big 4 (Deloitte, PwC, EY, KPMG)',
                                              'Investment Banks', 'Consulting Firms', 'FinTech']
        else:
            output['recommended_companies'] = ['Research target companies based on your career goals']
        
        # Learning resources
        output['learning_resources'] = {
            'online_courses': ['Coursera', 'Udemy', 'edX', 'NPTEL', 'LinkedIn Learning'],
            'practice_platforms': ['LeetCode', 'HackerRank', 'GeeksforGeeks', 'Kaggle', 'GitHub'],
            'networking': ['LinkedIn', 'AngelList', 'Meetup', 'Industry Conferences'],
            'career_prep': ['Glassdoor', 'AmbitionBox', 'Indeed', 'Naukri.com']
        }
        
        return output
    
    def _generate_detailed_roadmap(self, career: str, stream: str) -> Dict:
        """Generate detailed career roadmap for Stage 2"""
        roadmap = {
            'career': career,
            'current_stage': 'Class 10-12',
            'milestones': []
        }
        
        # Define roadmap based on career
        if 'Engineer' in career or 'Software' in career:
            roadmap['milestones'] = [
                {'stage': 'Class 11-12', 'focus': 'Physics, Chemistry, Mathematics', 
                 'actions': ['Score 90%+', 'Start JEE preparation', 'Learn basic programming']},
                {'stage': 'Entrance Exams', 'focus': 'JEE Main/Advanced', 
                 'actions': ['Clear JEE with good rank', 'Apply to top colleges']},
                {'stage': 'B.Tech Year 1-2', 'focus': 'Core subjects + coding', 
                 'actions': ['Build strong fundamentals', 'Start competitive programming', 'First internship']},
                {'stage': 'B.Tech Year 3-4', 'focus': 'Specialization + projects', 
                 'actions': ['Multiple internships', 'Build portfolio', 'Prepare for placements']},
                {'stage': 'Post-Graduation', 'focus': 'Job or MS', 
                 'actions': ['Secure placement', 'Or apply for MS abroad']}
            ]
        elif 'Doctor' in career or 'Medical' in career:
            roadmap['milestones'] = [
                {'stage': 'Class 11-12', 'focus': 'Biology, Chemistry, Physics', 
                 'actions': ['Score 95%+', 'Start NEET preparation', 'Understand medical ethics']},
                {'stage': 'NEET Exam', 'focus': 'NEET UG', 
                 'actions': ['Clear NEET with high score', 'Apply to top medical colleges']},
                {'stage': 'MBBS (5.5 years)', 'focus': 'Medical education + internship', 
                 'actions': ['Complete all rotations', '1-year internship', 'Pass all exams']},
                {'stage': 'Post-MBBS', 'focus': 'Practice or specialization', 
                 'actions': ['NEET PG for MD/MS', 'Or start practice']}
            ]
        elif 'CA' in career or 'Accountant' in career:
            roadmap['milestones'] = [
                {'stage': 'Class 11-12', 'focus': 'Commerce subjects', 
                 'actions': ['Score well', 'Register for CA Foundation', 'Understand accounting basics']},
                {'stage': 'CA Foundation', 'focus': 'First level exam', 
                 'actions': ['Clear in first attempt', 'Start Intermediate preparation']},
                {'stage': 'CA Intermediate + Articleship', 'focus': '3 years practical training', 
                 'actions': ['Clear Intermediate', 'Complete articleship', 'Gain real experience']},
                {'stage': 'CA Final', 'focus': 'Final exam', 
                 'actions': ['Clear CA Final', 'Become Chartered Accountant']},
                {'stage': 'Post-CA', 'focus': 'Career growth', 
                 'actions': ['Join Big 4', 'Or start practice', 'Consider CFA/MBA']}
            ]
        else:
            roadmap['milestones'] = [
                {'stage': 'Class 11-12', 'focus': 'Academic excellence', 
                 'actions': ['Score well', 'Identify entrance exams', 'Build profile']},
                {'stage': 'Entrance/Selection', 'focus': 'Get into good college', 
                 'actions': ['Clear entrance exams', 'Apply strategically']},
                {'stage': 'Undergraduate', 'focus': 'Skill building', 
                 'actions': ['Internships', 'Projects', 'Networking']},
                {'stage': 'Career Launch', 'focus': 'Job or higher studies', 
                 'actions': ['Placements', 'Or further education']}
            ]
        
        return roadmap
    
    def _get_immediate_actions(self, inputs: Dict) -> List[str]:
        """Get immediate actions for UG students"""
        actions = []
        
        if not inputs['internships']:
            actions.append("🚨 PRIORITY: Apply for internships immediately")
        
        if not inputs['personal_projects']:
            actions.append("🔨 Start building personal projects")
        
        if not inputs['has_cv']:
            actions.append("📄 Create professional CV/Resume")
        
        if len(inputs['technical_skills']) < 5:
            actions.append("📚 Learn in-demand skills through online courses")
        
        if not inputs['certifications']:
            actions.append("🎓 Complete relevant certifications")
        
        if inputs['cgpa'] < 7.0:
            actions.append("📈 Focus on improving academic performance")
        
        if not actions:
            actions.append("✅ Continue current trajectory, explore advanced opportunities")
        
        return actions
    
    def print_stage1_report(self, output: Dict):
        """Print Stage 1 Exploration Report"""
        print("\n" + "="*80)
        print("📊 EXPLORATION REPORT - STAGE 1")
        print("="*80)
        print(f"\nStudent: {output['student_name']}")
        print(f"Grade: {output['grade']}")
        print(f"Stage: {output['stage']}")
        
        report = output['exploration_report']
        print("\n" + "─"*80)
        print("🎯 IDENTIFIED INTERESTS & INCLINATIONS")
        print("─"*80)
        print(f"\n📚 Subject Inclinations: {', '.join(report['subject_inclinations'])}")
        print(f"🎨 Creative Interests: {', '.join(report['creative_interests'])}")
        print(f"🏆 Achievements: {', '.join(report['achievements']) if report['achievements'] else 'None yet - keep exploring!'}")
        
        print(f"\n💡 Personality Insights:")
        print(f"   Type: {report['personality_insights']['type']}")
        print(f"   Strengths: {', '.join(report['personality_insights']['strengths'])}")
        
        print("\n" + "─"*80)
        print("🌟 SUGGESTED PATHWAYS TO EXPLORE")
        print("─"*80)
        for i, pathway in enumerate(output['suggested_pathways'], 1):
            print(f"   {i}. {pathway}")
        
        print("\n" + "─"*80)
        print("👀 CAREER AWARENESS (Fields to Explore - No Pressure!)")
        print("─"*80)
        for insight in output['awareness_insights']:
            print(f"   • {insight}")
        
        print("\n" + "─"*80)
        print("🎪 CLUBS & WORKSHOPS TO JOIN")
        print("─"*80)
        for club in output['clubs_workshops']:
            print(f"   • {club}")
        
        print("\n" + "─"*80)
        print("💬 GUIDANCE NOTE")
        print("─"*80)
        print("""
   At this stage, the focus is on EXPLORATION, not decision-making.
   
   ✓ Try different activities and subjects
   ✓ Participate in competitions and projects
   ✓ Discover what excites and energizes you
   ✓ Don't worry about choosing a final career yet
   ✓ Build diverse skills and experiences
   
   Remember: This is YOUR journey of discovery! 🚀
        """)
        print("="*80)
    
    def print_stage2_report(self, output: Dict):
        """Print Stage 2 Career Prediction Report"""
        print("\n" + "="*80)
        print("🎯 CAREER PREDICTION & ROADMAP - STAGE 2")
        print("="*80)
        print(f"\nStudent: {output['student_name']}")
        print(f"Grade: {output['grade']}")
        print(f"Stream: {output['stream']}")
        print(f"Stage: {output['stage']}")
        
        print("\n" + "─"*80)
        print("🏆 TOP RECOMMENDED CAREERS")
        print("─"*80)
        for i, career in enumerate(output['predicted_careers'], 1):
            print(f"   {i}. {career}")
        
        print("\n" + "─"*80)
        print("🔄 ALTERNATE/BACKUP CAREERS")
        print("─"*80)
        for career in output['alternate_careers']:
            print(f"   • {career}")
        
        print("\n" + "─"*80)
        print("📝 COMPETITIVE EXAMS TO TARGET")
        print("─"*80)
        for exam in output['competitive_exams']:
            print(f"   • {exam}")
        
        print("\n" + "─"*80)
        print("🎯 SKILLS TO DEVELOP")
        print("─"*80)
        for skill in output['skills_to_develop']:
            print(f"   • {skill}")
        
        print("\n" + "─"*80)
        print("💼 INTERNSHIP RECOMMENDATIONS")
        print("─"*80)
        for rec in output['internship_recommendations']:
            print(f"   • {rec}")
        
        print("\n" + "─"*80)
        print("🎓 HIGHER EDUCATION PATHS")
        print("─"*80)
        for path in output['higher_education_paths']:
            print(f"   • {path}")
        
        # Print detailed roadmap
        if output['career_roadmap']:
            print("\n" + "="*80)
            print(f"🗺️  DETAILED CAREER ROADMAP: {output['career_roadmap']['career']}")
            print("="*80)
            
            for milestone in output['career_roadmap']['milestones']:
                print(f"\n📍 {milestone['stage']}")
                print(f"   Focus: {milestone['focus']}")
                print(f"   Actions:")
                for action in milestone['actions']:
                    print(f"      • {action}")
        
        print("\n" + "="*80)
    
    def print_stage3_report(self, output: Dict):
        """Print Stage 3 Career Readiness Report"""
        print("\n" + "="*80)
        print("🚀 CAREER MAPPING & EMPLOYABILITY REPORT - STAGE 3")
        print("="*80)
        print(f"\nStudent: {output['student_name']}")
        print(f"Degree: {output['degree']}")
        print(f"Stage: {output['stage']}")
        
        print("\n" + "─"*80)
        print(f"📊 EMPLOYABILITY SCORE: {output['employability_score']}/100")
        print("─"*80)
        
        readiness = output['job_readiness']
        print(f"\n✓ Technical Readiness: {readiness['technical_readiness']}")
        print(f"✓ Experience Level: {readiness['experience_level']}")
        print(f"✓ Profile Strength: {readiness['profile_strength']}")
        
        print("\n" + "─"*80)
        print("🎯 CAREER MAPPING (Employability Focus)")
        print("─"*80)
        for i, career in enumerate(output['career_mapping'], 1):
            print(f"   {i}. {career}")
        
        # Skill gap analysis
        if output['skill_gap_analysis']:
            gap = output['skill_gap_analysis']
            print("\n" + "─"*80)
            print(f"📈 SKILL GAP ANALYSIS - Target: {gap['target_career']}")
            print("─"*80)
            
            print(f"\n✅ Skills You Have:")
            for skill in gap['skills_you_have']:
                print(f"   ✓ {skill}")
            
            print(f"\n📚 Skills to Develop:")
            for skill in gap['skills_to_develop']:
                print(f"   → {skill}")
            
            if gap['additional_skills']:
                print(f"\n⭐ Additional Skills (Bonus):")
                for skill in gap['additional_skills']:
                    print(f"   + {skill}")
        
        # Graduate pathways
        pathways = output['graduate_pathways']
        print("\n" + "─"*80)
        print(f"🎓 GRADUATE PATHWAY: {pathways['primary']}")
        print("─"*80)
        print(f"\nFocus: {pathways['focus']}")
        print(f"Timeline: {pathways['timeline']}")
        print(f"\nAction Plan:")
        for action in pathways['actions']:
            print(f"   • {action}")
        
        # Resume enhancement
        print("\n" + "─"*80)
        print("📄 RESUME ENHANCEMENT SUGGESTIONS")
        print("─"*80)
        for suggestion in output['resume_enhancement']:
            print(f"   {suggestion}")
        
        # Immediate actions
        print("\n" + "─"*80)
        print("🚨 IMMEDIATE ACTIONS REQUIRED")
        print("─"*80)
        for action in readiness['immediate_actions']:
            print(f"   {action}")
        
        # Company recommendations
        print("\n" + "─"*80)
        print("🏢 TARGET COMPANIES/SECTORS")
        print("─"*80)
        for company in output['recommended_companies']:
            print(f"   • {company}")
        
        # Learning resources
        print("\n" + "─"*80)
        print("📚 LEARNING RESOURCES")
        print("─"*80)
        resources = output['learning_resources']
        print(f"\n🎓 Online Courses: {', '.join(resources['online_courses'])}")
        print(f"💻 Practice Platforms: {', '.join(resources['practice_platforms'])}")
        print(f"🤝 Networking: {', '.join(resources['networking'])}")
        print(f"💼 Career Prep: {', '.join(resources['career_prep'])}")
        
        print("\n" + "="*80)
    
    def save_report(self, output: Dict, filename: str = None):
        """Save report to JSON file"""
        if not filename:
            student_name = output.get('student_name', 'student').replace(' ', '_')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"NaviRiti_Report_{student_name}_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=4, ensure_ascii=False)
        
        print(f"\n✅ Report saved successfully: {filename}")
        return filename


def main():
    """Main function to run NaviRiti Career Prediction System"""
    print("╔" + "═"*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + " "*20 + "NaviRiti - Career Guidance System" + " "*25 + "║")
    print("║" + " "*25 + "Phase 1 (Release 1.0)" + " "*33 + "║")
    print("║" + " "*15 + "Complete Student-Centric Prediction Model" + " "*22 + "║")
    print("║" + " "*78 + "║")
    print("╚" + "═"*78 + "╝")
    print()
    
    predictor = NaviRitiCareerPredictor()
    
    # Get basic information
    print("👤 BASIC INFORMATION")
    print("─"*80)
    name = input("Student Name: ").strip()
    while True:
        try:
            grade = int(input("Current Grade/Year (6-20): "))
            if 6 <= grade <= 20:
                break
            print("⚠️  Please enter a valid grade between 6 and 20")
        except ValueError:
            print("⚠️  Please enter a valid number")
    
    stage = predictor.get_student_stage(grade)
    print(f"\n✅ Identified Stage: {stage}\n")
    
    # Collect stage-specific inputs
    if "Stage 1" in stage:
        inputs = predictor.collect_stage1_inputs()
        output = predictor.generate_stage1_output(name, grade, inputs)
        predictor.print_stage1_report(output)
        
    elif "Stage 2" in stage:
        inputs = predictor.collect_stage2_inputs()
        output = predictor.generate_stage2_output(name, grade, inputs)
        predictor.print_stage2_report(output)
        
    elif "Stage 3" in stage:
        inputs = predictor.collect_stage3_inputs()
        output = predictor.generate_stage3_output(name, inputs)
        predictor.print_stage3_report(output)
    
    # Save report
    print("\n" + "─"*80)
    save = input("Would you like to save this report? (yes/no): ").lower()
    if save == 'yes':
        predictor.save_report(output)
    
    print("\n" + "="*80)
    print("Thank you for using NaviRiti Career Guidance System!")
    print("For Phase 2 features: Live Consultations, Detailed Roadmaps, Well-being Detection")
    print("="*80)


if __name__ == "__main__":
    main()