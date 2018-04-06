import os

articles = os.listdir('./articles/')
# articles.remove('.DS_Store')

amp_head = open('./templates/head.txt', 'r')
amp_foot = open('./templates/foot.txt', 'r')
head = amp_head.read()
foot = amp_foot.read()

for a in articles:
  path = './articles/' + a
  article = open(path, 'r')
  article_string = article.read()
  article.close()
  full_html = head + article_string + foot

  a = a.replace('txt', 'html')
  name = './amp-pages/' + a
  full = open(name, 'w')
  full.write(full_html)
  full.close()

amp_head.close()
amp_foot.close()



