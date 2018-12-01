from pymongo import MongoClient
from validate_email import validate_email

myclient = MongoClient()
mydb = myclient["mini3"]
mycol = mydb["history"]
# mydict = [{"email": "harry@126.com", "ctype": "@username", "content": "Taylor", "num": 18},
#           {"email": "harry@126.com", "ctype": "#hashtag", "content": "basketball", "num": 10},
#           {"email": "harry@gmail.com", "ctype": "@username", "content": "Bakeham", "num": 23},
#           {"email": "Joe@gmail.com", "ctype": "#hashtag", "content": "football", "num": 5},
#           {"email": "matty@126.com", "ctype": "@username", "content": "Taylor", "num": 18},
#           {"email": "matty@126.com", "ctype": "@username", "content": "Taylor", "num": 25},
#           {"email": "mat@126.com", "ctype": "#hashtag", "content": "basketball", "num": 18},]
# mycol.insert_many(mydict)



u = str()
while u != 'quit':

        print('Filter:[FullData(0)][email(1)][SearchType(2)][SearchContents(3)][NumberOfImages(4)][MostPopular(5)][quit(q)]')
        u = input('choose by typing the number according to the order:')

        if u == '0':
            print('FullData:\n')
            a = 0
            b = 0
            data = mycol.find()
            for i in data:
                print(i)
                a += i['num']
                b += 1
            avg = a/b
            print("Average Number of Images Per Feed:", avg)

        if u == '1':
            email = input('filtering by email:')
            if not validate_email(email):
                raise ValueError('NOT VALID!')
            data = mycol.find({'email':email})
            for i in data:
                print(i)

        if u == '2':
            ctype = input('filtering by SearchType:@username/#hashtag(u/h)')
            if ctype == 'u':
                data = mycol.find({'ctype': '@username'})
                for i in data:
                    print(i)
            elif ctype == 'h':
                data = mycol.find({'ctype': '#hashtag'})
                for i in data:
                    print(i)

        if u == '3':
            content = input('filtering by content:')
            data = mycol.find({'content': {'$regex': content}})
            for i in data:
                print(i)

        if u == '4':
            display = input('filtering by Number of Images: Ascending/Descending(A/D)')
            if display == 'A':
                data = mycol.find().sort("num")
                for i in data:
                    print(i)

            elif display == 'D':
                data = mycol.find().sort("num", -1)
                for i in data:
                    print(i)

        if u == '5':
            w = input('Most Popular Contents:Ascending/Descending(A/D)')
            data = mycol.find()
            rank = {}
            for i in data:
                if i['content'] in rank:
                    rank[i['content']] += 1
                else:
                    rank[i['content']] = 1
            if w == 'A':
                a = [(k, rank[k]) for k in sorted(rank, key=rank.get, reverse=False)]
                print(a)

            elif w == 'D':
                d = [(k, rank[k]) for k in sorted(rank, key=rank.get, reverse=True)]
                print(d)

        if u == 'q':
            u = 'quit'