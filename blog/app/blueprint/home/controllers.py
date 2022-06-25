from flask import Blueprint, render_template, current_app


home = Blueprint("home", __name__, template_folder="templates", static_folder="static")

# fake database here
blog_post = [
    {
        "blog-thumb": "images/blog-post-01.jpg",
        "alt-thumb": "blog-post-01",
        "kategori": "Lifestyle",
        "judul": "Best Template Website for HTML CSS",
        "author": {"Admin": "#admin"},
        "tanggal": "May 31, 2020",
        "comment": 12,
        "text": """Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template collection site for the download purpose.""",
        "tags": {"Beauty": "#beauty", "Nature": "#nature"},
    },
    {
        "blog-thumb": "images/blog-post-02.jpg",
        "alt-thumb": "blog-post-02",
        "kategori": "Healthy",
        "judul": "Etiam id diam vitae lorem dictum",
        "author": {"Admin": "#admin"},
        "tanggal": "May 31, 2020",
        "comment": 12,
        "text": """Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template collection site for the download purpose.""",
        "tags": {"Best Templates": "#besttemplates", "TemplateMo": "#TemplateMo"},
    },
    {
        "blog-thumb": "images/blog-post-03.jpg",
        "alt-thumb": "blog-post-03",
        "kategori": "Fashion",
        "judul": "Donec tincidunt leo nec magna",
        "author": {"Admin": "#admin"},
        "tanggal": "May 31, 2020",
        "comment": 12,
        "text": """Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template collection site for the download purpose.""",
        "tags": {"HTML CSS": "#HTMLCSS", "Photoshop": "#Photoshop"},
    },
    {
        "blog-thumb": "images/blog-post-01.jpg",
        "alt-thumb": "blog-post-01",
        "kategori": "Lifestyle",
        "judul": "Best Template Website for HTML CSS",
        "author": {"Admin": "#admin"},
        "tanggal": "May 31, 2020",
        "comment": 12,
        "text": """Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template collection site for the download purpose.""",
        "tags": {"Beauty": "#beauty", "Nature": "#nature"},
    },
    {
        "blog-thumb": "images/blog-post-02.jpg",
        "alt-thumb": "blog-post-02",
        "kategori": "Healthy",
        "judul": "Etiam id diam vitae lorem dictum",
        "author": {"Admin": "#admin"},
        "tanggal": "May 31, 2020",
        "comment": 12,
        "text": """Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template collection site for the download purpose.""",
        "tags": {"Best Templates": "#besttemplates", "TemplateMo": "#TemplateMo"},
    },
    {
        "blog-thumb": "images/blog-post-03.jpg",
        "alt-thumb": "blog-post-03",
        "kategori": "Fashion",
        "judul": "Donec tincidunt leo nec magna",
        "author": {"Admin": "#admin"},
        "tanggal": "May 31, 2020",
        "comment": 12,
        "text": """Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template collection site for the download purpose.""",
        "tags": {"HTML CSS": "#HTMLCSS", "Photoshop": "#Photoshop"},
    },
]

recent_post = [
    {
        "judul": "Vestibulum id turpis porttitor sapien facilisis scelerisque",
        "link": "#post-details",
        "tanggal": "May 31, 2020",
    },
    {
        "judul": "Suspendisse et metus nec libero ultrices varius eget in risus",
        "link": "#post-details",
        "tanggal": "May 31, 2020",
    },
    {
        "judul": "Swag hella echo park leggings, shaman cornhole ethical coloring",
        "link": "#post-details",
        "tanggal": "May 31, 2020",
    },
]

categories = {
    "Nature Lifestyle": "#NatureLifestyle",
    "Awesome Layouts": "#AwesomeLayouts",
    "Creative Ideas": "#CreativeIdeas",
    "Responsive Templates": "#ResponsiveTemplates",
    "HTML5 / CSS3 Templates": "#HTML5CSS3Templates",
    "Creative & Unique": "#CreativeUnique",
}

tags = {
    "Lifestyle": "#Lifestyle",
    "Creative": "#Creative",
    "HTML5": "#HTML5",
    "Inspiration": "#Inspiration",
    "Motivation": "#Motivation",
    "PSD": "#PSD",
    "Responsive": "#Responsive",
}


@home.route("/")
def index():
    # print([i for i in current_app.db["post"].find({})])  # database testing

    return render_template(
        "home.html",
        blog_post=blog_post,
        recent_post=recent_post,
        categories=categories,
        tags=tags,
    )
