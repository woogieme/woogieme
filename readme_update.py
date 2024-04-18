import feedparser,datetime

# rss 추출
feed = feedparser.parse("https://woogieme.tistory.com/rss") 

# README 양식
markdown_text = """

<div align="center">

# Back-End Developer

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fleemember&count_bg=%23FDC8F8CB&title_bg=%23F54D4D96&icon=smugmug.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/woogieme)


## ✨ Back-end Stack ✨

<div>
<img src="https://img.shields.io/badge/Java-E34F26?style=flat-square&logo=Java&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-F68212?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/SpringBoot-CC6699?style=flat-square&logo=SpringBoot&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-61DAFB?style=flat-square&logo=MySQL&logoColor=white"/>
<img src="https://img.shields.io/badge/HTML-764ABC?style=flat-square&logo=HTML5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-FF9955?style=flat-square&logo=CSS3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/>
</br>
</div>

## ✨ Cowork tools ✨

<div>
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
<img src="https://img.shields.io/badge/Notion-FFE4AF?style=flat-square&logo=Notion&logoColor=black"/>
<img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=Postman&logoColor=white"/>
</div>
  
<br />

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=woogieme&show_icons=true&theme=dracula)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=woogieme&layout=compact)](https://github.com/woogieme/github-readme-stats)

</div>

<br>

### 📕 Latest Blog Posts   

""" # list of blog posts will be appended here

for i in feed['entries'][:5]:
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"
    #print(i['link'], i['title'])

#print(markdown_text)
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()




