import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title="My webpage", page_icon=":seedling:", layout="wide")

st.write('<style>div.block-container{padding-bottom:2rem;}</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_intro = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_sy6mqjxk.json")
lottie_footer = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_wlSAOz.json")
with open("content/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
            <link rel="stylesheet" href="assets/css/style.css">
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">""",
            unsafe_allow_html=True)

css = """
<style>
body {
    margin-bottom: 0;
    padding-bottom: 0;
}
.footer {
    margin-top: 0;
    padding-top: 0;
}
</style>
"""

# Render the CSS styles
st.markdown(css, unsafe_allow_html=True)

















# part-1 navigation bar===========================================
st.markdown('<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+7V1pXEw6D+7a0t5gkfsloR8yC/J2m8i3vEf83MUNI8RqK1" crossorigin="anonymous"></script>', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #ffffff;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#nirali-singh" style="color: #000000; font-size: 17px">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#latest-edition" style="color: #000000; font-size: 17px">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience" style="color: #000000; font-size: 17px">Resume</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#let-s-connect" style="color: #000000; font-size: 17px">Let's connect</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


##############    INTRODUCTION    ###################
with st.container():
    left_col, right_col = st.columns(2)
    with left_col:
        st.write(
        '''
        <div class="name-heading" style="margin-top: -20px;">Nirali Singh</div>
        <div class="job_title">Data Analyst</div>''',unsafe_allow_html=True)
        st.write('''<div class="summary">Data Analyst with a passion for discovering insights from complex data, skilled in utilizing Python, SQL, and Excel, coupled with strong analytical and research skills, to verify, manage, and analyze data to drive accurate and meaningful business results with a focus on meeting the needs of clients and stakeholders. Proficient in data mining and visualization with the help of BI tools, to effectively communicate insights and successfully execute projects.</div>
        ''', unsafe_allow_html=True)
        
    with right_col:
        st.markdown("""
                    <div class="intro-link-basic">
                        <div>
                            <div class="social"><a href="https://www.linkedin.com/in/niralisingh/"><i class="icon ion-social-linkedin"></i></a><a href="https://github.com/Nirali227"><i class="icon ion-social-github"></i></a><a href="mailto:nirali2270@gmail.com"><i class="material-icons">email</i></a></div>
                            </div>
                    </div>
                    """,unsafe_allow_html=True)
        st_lottie(lottie_intro, height=360, key="coding")
        

##################   SKILL SECTION    ##############################
st.write(' ')
st.write(' ')
st.write('---')
with st.container():
    st.write('''
    <div class="skills">Skills</div>
    ''',unsafe_allow_html= True)
    skill_col1, skill_col2 = st.columns(2)
    with skill_col1:
        st.markdown("- Database: MySQL, MongoDB")
        st.markdown("- Programming Skills: Python")
        st.markdown("- Statistical Analysis: Descriptive Statistics, Hypothesis Testing")
        

    with skill_col2:
        st.markdown("- Data Analysis: Pandas, NumPy, Jupyter")
        st.markdown("- Web Scraping: BeautifulSoup, Selenium, Requests")
        st.markdown("- Data Visualizations: Microsoft Power BI, Excel, Matplotlib, Seaborn")

####################    PROJECTS    ######################
st.write(' ')
st.write(' ')
st.write('---')
with st.container():
    st.write('<div class="project_heading">Latest Projects</div>',unsafe_allow_html=True)

with st.container():    
    col1, col2 = st.columns([1.5,3])
    with col1:
        st.write(' ')
        st.write(' ')
        im2 = st.image(Image.open("content/images/images/10.jpg"))
        st.write(' ')
        st.write(' ')  
    with col2:
        st.write('<div class="project">Web Scraping Project: Competitive Analysis of E-Commerce Site</div>',unsafe_allow_html=True)
        st.write('''
                    <div class="project_desc">Tools used: Python, Exceldf dsghgukjh gfuiodklng huiofklde jrkhgiufo dk;lmf giouhd ekj lr g kiufodpjk an d Power BI</br>
                    This is bullj dkf hdi jkfehuji dkjehgy uivfkjn rhegufb iofu hejbre gjdfjherwe gjfkeoijef ghhu et one</br> 
                    this is budk lj ghi ufokl dmfgjf ikod;lem,rnhj fkd;lmnrkjflkd ,mkjl let two</br>
                    this is bulf sudi akjhekguifo ds;angiue ro wkql,j ghuifod ;l.,l et three</br>
                    </div>''',unsafe_allow_html=True)
        st.markdown("""
                    <div class="read-more-container">
                        <div class="read-more">
                            <div>
                                <div class="click-here"><a href="https://www.linkedin.com/in/niralisingh/">Read more</a></div>
                                </div>
                        </div>
                    </div>
                    """,unsafe_allow_html=True)

st.write('---')

with st.container():    
    col1, col2 = st.columns([1.5,3])
    with col1:
        st.write(' ')
        st.write(' ')
        im2 = st.image(Image.open("content/images/images/10.jpg"))
        st.write(' ')
        st.write(' ') 
    with col2:
        st.write('<div class="project">Web Scraping Project: Competitive Analysis of E-Commerce Site</div>',unsafe_allow_html=True)
        st.write('''
                    <div class="project_desc">Tools used: Python, Exceldf dsghgukjh gfuiodklng huiofklde jrkhgiufo dk;lmf giouhd ekj lr g kiufodpjk an d Power BI</br>
                    This is bullj dkf hdi jkfehuji dkjehgy uivfkjn rhegufb iofu hejbre gjdfjherwe gjfkeoijef ghhu et one</br> 
                    this is budk lj ghi ufokl dmfgjf ikod;lem,rnhj fkd;lmnrkjflkd ,mkjl let two</br>
                    this is bulf sudi akjhekguifo ds;angiue ro wkql,j ghuifod ;l.,l et three</br>
                    </div>''',unsafe_allow_html=True)
        st.markdown("""
                    <div class="read-more-container">
                        <div class="read-more">
                            <div>
                                <div class="click-here"><a href="project1.py"">Read more</a></div>
                                </div>
                        </div>
                    </div>
                    """,unsafe_allow_html=True)

st.write('---')

with st.container():    
    col1, col2 = st.columns([1.5,3])
    with col1:
        st.write(' ')
        st.write(' ')
        im2 = st.image(Image.open("content/images/images/10.jpg"))
        st.write(' ')
        st.write(' ')  
    with col2:
        st.write('<div class="project">Web Scraping Project: Competitive Analysis of E-Commerce Site</div>',unsafe_allow_html=True)
        st.write('''
                    <div class="project_desc">Tools used: Python, Exceldf dsghgukjh gfuiodklng huiofklde jrkhgiufo dk;lmf giouhd ekj lr g kiufodpjk an d Power BI</br>
                    This is bullj dkf hdi jkfehuji dkjehgy uivfkjn rhegufb iofu hejbre gjdfjherwe gjfkeoijef ghhu et one</br> 
                    this is budk lj ghi ufokl dmfgjf ikod;lem,rnhj fkd;lmnrkjflkd ,mkjl let two</br>
                    this is bulf sudi akjhekguifo ds;angiue ro wkql,j ghuifod ;l.,l et three</br>
                    </div>''',unsafe_allow_html=True)
        st.markdown("""
                    <div class="read-more-container">
                        <div class="read-more">
                            <div>
                                <div class="click-here"><a href="https://www.linkedin.com/in/niralisingh/">Read more</a></div>
                                </div>
                        </div>
                    </div>
                    """,unsafe_allow_html=True)


##################    CONNECT SECTION     ###############################

with st.container():
    st.write('---')
    st.write('''
            <div class="connect_head">Let's connect</div>''',unsafe_allow_html=True)
    st.write('''
            <div class="footer-basic">
                    <div>
                        <div class="social"><a href="https://www.linkedin.com/in/niralisingh/"><i class="icon ion-social-linkedin"></i></a><a href="https://github.com/Nirali227"><i class="icon ion-social-github"></i></a><a href="mailto:nirali2270@gmail.com"><i class="material-icons">email</i></a></div>
                        <ul class="list-inline">
                            <li class="list-inline-item"><a href="#">Home</a></li>
                            <li class="list-inline-item"><a href="#">Projects</a></li>
                            <li class="list-inline-item"><a href="#">Resume</a></li>
                        </ul>
                    </div>''',unsafe_allow_html=True)
























