import db

sql = ("INSERT INTO rp_characters VALUES(null, %s, %s, %s, %s, %s, %s, NOW(), NOW())")
data = ('mouse cop', 23, '5', '124', 'human', '#1234')

query(sql, data)