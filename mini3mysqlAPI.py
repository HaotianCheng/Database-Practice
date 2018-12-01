import mysql.connector
from validate_email import validate_email

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='mini3'
)

mycursor = mydb.cursor()

u = str()
while u != 'quit':

        print('Filter:[FullData(0)][email(1)][SearchType(2)][SearchContents(3)][NumberOfImages(4)][MostPopular(5)][quit(q)]')
        u = input('choose by typing the number according to the order:')

        if u == '0':
            print('FullData:\n')
            sql = "SELECT * FROM history"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            a = 0
            for i in myresult:
                a += i[3]
                print(i)
            avg = a/len(myresult)
            print("Average Number of Images Per Feed:", avg)

        if u == '1':
            email = input('filtering by email:')
            if not validate_email(email):
                raise ValueError('NOT VALID!')
            email = '"%s"' % email
            sql = "SELECT * FROM history WHERE email = " + email
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for i in myresult:
                print(i)

        if u == '2':
            ctype = input('filtering by SearchType:@username/#hashtag(u/h)')
            if ctype == 'u':
                sql = "SELECT * FROM history WHERE type = '@username'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for i in myresult:
                    print(i)
            elif ctype == 'h':
                sql = "SELECT * FROM history WHERE type = '#hashtag'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for i in myresult:
                    print(i)

        if u == '3':
            content = input('filtering by content:')
            content = '"%' + content + '%"'
            sql = "SELECT * FROM history WHERE content LIKE " + content
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for i in myresult:
                print(i)

        if u == '4':
            display = input('filtering by Number of Images: Ascending/Descending(A/D)')
            if display == 'A':
                sql = "SELECT * FROM history ORDER BY num"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for i in myresult:
                    print(i)

            elif display == 'D':
                sql = "SELECT * FROM history ORDER BY num DESC"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for i in myresult:
                    print(i)

        if u == '5':
            w = input('Most Popular Contents:Ascending/Descending(A/D)')
            sql = "SELECT * FROM history"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            rank = {}
            for i in myresult:
                if i[1] in rank:
                    rank[i[1]] += 1
                else:
                    rank[i[1]] = 1
            if w == 'A':
                a = [(k, rank[k]) for k in sorted(rank, key=rank.get, reverse=False)]
                print(a)

            elif w == 'D':
                d = [(k, rank[k]) for k in sorted(rank, key=rank.get, reverse=True)]
                print(d)

        if u == 'q':
            u = 'quit'