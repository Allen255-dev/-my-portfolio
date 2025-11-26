from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Personal information
PERSONAL_INFO = {
    'name': 'Dev Allen',
    'title': 'Python Developer',
    'bio': 'I build amazing web applications with Python and Flask',
    'email': 'amegwu255@gmail.com',
    'phone': '+2347047013669',
    'whatsapp': '+2347047013669',
    'location': 'Owerri, Nigeria',
    'about_me': 'I am a passionate Python developer with experience in building web applications using Flask. I love creating efficient and scalable solutions.',
    'profile_image': 'profile.jpg'
}

SOCIAL_LINKS = {
    'github': 'https://github.com/Allen255-dev',
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'twitter': 'https://twitter.com/yourhandle',
    'whatsapp': 'https://wa.me/qr/OCQHIFKK2EECM1'
}

# Projects data
PROJECTS = [
    {
        'id': 1,
        'title': 'Analog Clock',
        'description': 'A clean and functional analog clock built with HTML, CSS, and JavaScript.',
        'image': 'project1.jpg',
        'technologies': ['HTML5', 'CSS3', 'JavaScript'],
        'github_url': 'https://github.com/Allen255-dev/analog-clock',
        'live_url': 'https://allen255-dev.github.io/analog-clock/',
        'featured': True
    },
    {
        'id': 2,
        'title': 'Task Management App',
        'description': 'A productivity app for managing daily tasks',
        'image': 'project2.jpg',
        'technologies': ['Python', 'Flask', 'SQLite', 'Bootstrap'],
        'github_url': 'https://github.com/yourusername/project2',
        'live_url': 'https://yourapp.com',
        'featured': True
    },
    {
        'id': 3,
        'title': 'Weather App',
        'description': 'Real-time weather application',
        'image': 'project3.jpg',
        'technologies': ['Python', 'Flask', 'API', 'JavaScript'],
        'github_url': 'https://github.com/yourusername/project3',
        'live_url': 'https://weatherapp.com',
        'featured': True
    }
]

@app.route('/')
def home():
    featured_projects = [p for p in PROJECTS if p.get('featured', True)][:3]
    return render_template('index.html', 
                         current_year=datetime.now().year,
                         projects=featured_projects,
                         personal_info=PERSONAL_INFO,
                         social_links=SOCIAL_LINKS)

@app.route('/about')
def about():
    skills = {
        'Languages': ['Python', 'JavaScript', 'HTML/CSS', 'SQL'],
        'Frameworks': ['Flask', 'Django', 'Bootstrap'],
        'Tools': ['Git', 'VS Code', 'PostgreSQL', 'MongoDB'],
        'Other': ['Web Development', 'API Development', 'Data Analysis']
    }
    
    return render_template('about.html', 
                         skills=skills,
                         personal_info=PERSONAL_INFO,
                         social_links=SOCIAL_LINKS)

@app.route('/projects')
def projects():
    return render_template('projects.html', 
                         projects=PROJECTS,
                         personal_info=PERSONAL_INFO,
                         social_links=SOCIAL_LINKS)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_detail.html', 
                         project=project,
                         personal_info=PERSONAL_INFO,
                         social_links=SOCIAL_LINKS)

@app.route('/blog')  # ADDED THE MISSING BLOG ROUTE
def blog():
    # You can add blog posts data here later
    blog_posts = [
        {
            'title': 'Getting Started with Flask',
            'date': '2024-01-15',
            'excerpt': 'Learn how to build web applications with Flask...',
            'content': 'Full blog post content here...'
        },
        {
            'title': 'Python Tips and Tricks',
            'date': '2024-01-10',
            'excerpt': 'Useful Python tips for everyday coding...',
            'content': 'Full blog post content here...'
        }
    ]
    return render_template('blog.html',
                         blog_posts=blog_posts,
                         personal_info=PERSONAL_INFO,
                         social_links=SOCIAL_LINKS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"New message from {name} ({email}): {message}")
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html',
                         personal_info=PERSONAL_INFO,
                         social_links=SOCIAL_LINKS)

if __name__ == '__main__':
    app.run(debug=True, port=5001)