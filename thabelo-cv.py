#Defining a class and a constructor to initializes the attributes of the class when an instance is created.
class ThabeloCV:
    #Assigning paramaters to instance variables of the class. {they hold the data for the CV.}
    def __init__(self, name, contact_info, skills, certifications, summary, experience, education):
        self.name = name
        self.contact_info = contact_info
        self.skills = skills
        self.certifications = certifications
        self.summary = summary
        self.experience = experience
        self.education = education
#Displays the method which prints the CV details in the formatted way.
    def display_cv(self):
        print(f"Name: {self.name}\n")
        print(f"Contact Information:")
        for key, value in self.contact_info.items():
            print(f"  {key}: {value}")
        print("\nSkills:")
        for skill in self.skills:
            print(f"  • {skill}")
        print("\nLicenses & Certifications:")
        for category, certs in self.certifications.items():
            print(f"  {category}:")
            for cert in certs:
                print(f"    • {cert}")
        print("\nProfessional Summary:")
        print(f"  {self.summary}\n")
        print("Work Experience:")
        for job in self.experience:
            print(f"  {job['position']} at {job['company']} ({job['dates']})")
            for responsibility in job['responsibilities']:
                print(f"    • {responsibility}")
        print("\nEducation & Courses:")
        for course in self.education:
            print(f"  {course['title']} ({course['dates']})")
            for detail in course['details']:
                print(f"    • {detail}")
# Personal Information
name = "Thabelo Muthuvhukuma"
contact_info = {
    "Address": "1328 HoepHoep Crescent, Rabie Ridge, Midrand",
    "Phone": "0796537667",
    "E-mail": "thabelomuthuvhukuma@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/thabelo-muthuvhukuma-ab99bb205/",
    "Github": "https://github.com/Thabelo-M"
}

# Skills
skills = [
    "Python",
    "CI/CD",
    "Shell Scripting (Bash)",
    "Agile Development",
    "HTML, CSS & JavaScript"
]

# Certifications
certifications = {
    "AWS": [
        "AWS Cloud Practitioner",
        "AWS Certified Solutions Architect",
        "AWS Certified Developer Associate"
    ],
    "IBM Software Engineering & DevOps": [
        "IBM Python for Data Science, AI, AI Applications & Development",
        "IBM Agile Development & Scrum",
        "IBM Introduction to DevOps",
        "IBM Introduction to Cloud Computing",
        "IBM Linux Commands and Shell Scripting",
        "IBM Application Development using Microservices & Serverless",
        "IBM Continuous Integration and Continuous Delivery",
        "IBM Git and Github",
        "IBM Developing AI Applications with Python and Flask",
        "IBM Introduction to Containers w/ Docker, Kubernetes & OpenShift"
    ]
}

# Professional Summary
summary = (
    "As an AWS Facilitator with a strong background in teaching AWS fundamentals, I have a solid grasp of cloud technology "
    "and key AWS services. I am skilled in guiding individuals through essential AWS concepts and best practices. My training "
    "includes knowledge of designing scalable architectures, automating deployments, and managing cloud resources. I am "
    "enthusiastic about applying my technical knowledge and problem-solving skills to support cloud projects."
)

# Working Experience
experience = [
    {
        "position": "AWS FACILITATOR",
        "company": "Praesignis",
        "dates": "September 2022-Current",
        "responsibilities": [
            "-Oversee an intensive training course on the fundamentals of Amazon Web Services (AWS).",
            "-Guide students through engaging lectures and hands-on experiences.",
            "-Foster a collaborative environment for mastering essential cloud skills.",
            "-Aim to equip students for successful and fulfilling careers in the technology sector."
        ]
    },
    {
        "position": "JUNIOR DEVELOPER",
        "company": "Praesignis",
        "dates": "October 2021 – August 2022",
        "responsibilities": [
            "-Assisted the Full-Stack Developer in designing and implementing features for internal systems.",
            "-Played a role in sprint planning and retrospectives using Jira and Trello.",
            "-Contributed to both front-end and back-end development tasks.",
            "-Performed thorough testing to ensure software quality and functionality.",
            "-Actively engaged in the full software development lifecycle to deliver efficient and effective solutions."
        ]
    },
    {
        "position": "IT-Tech Support & AWS re/Start Learnership",
        "company": "Praesignis",
        "dates": "January 2021-September 2021",
        "responsibilities": [
            "-Earned IT-Tech Support and AWS Cloud Practitioner certifications",
            "-Demonstrated strong skills in technical support and foundational AWS cloud concepts"
        ]
    }
]

# Education & Courses
education = [
    {
        "title": "IBM DevOps and Software Engineering Professional Certificate",
        "dates": "February 2024-Current",
        "details": [
            "-Embrace DevOps: Use Agile and Scrum practices to streamline development and operations.",
            "-Build with Python: Develop applications using Python, focusing on functions, REST APIs, and libraries.",
            "-Work with Microservices: Create and deploy applications using microservices, containers like Docker and Kubernetes, and serverless options.",
            "-Automate & Integrate: Apply automation and continuous integration/deployment with tools such as Chef, Puppet, and GitHub Actions."
        ]
    }
]

# Create CV object and display it
my_cv = CV(name, contact_info, skills, certifications, summary, experience, education)
my_cv.display_cv()