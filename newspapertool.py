#!/usr/bin/env python3
import psycopg2
import datetime


def popular_three_articles():
    conn = psycopg2.connect(dbname='news')
    cur = conn.cursor()
    art = """SELECT articles.title , count(*) AS Views
    FROM articles JOIN log ON articles.slug = SUBSTRING(log.path, 10)
    GROUP BY  articles.title
    ORDER BY  Views DESC
    LIMIT 3;"""
    cur.execute(art)
    print("The Most Popular Three Articles Of All Time:")
    data = cur.fetchall()

    for row in data:
        print('"{}" -- {} Views'.format(row[0], row[1]))

    print("\n")
    cur.close()
    conn.close()


def most_popular_authors():
    conn = psycopg2.connect(dbname='news')
    cur = conn.cursor()
    art = """SELECT authors.name , count(*) AS View
    FROM articles JOIN log
    ON articles.slug = SUBSTRING(log.path, 10)
    JOIN authors
    ON articles.author = authors.id
    GROUP BY authors.name
    ORDER BY View DESC;"""
    cur.execute(art)
    print("The Most Popular Article Authors Of All Time Are:", cur.rowcount)
    data = cur.fetchall()

    for row in data:
        print('"{}" -- {} Views'.format(row[0], row[1]))

    print("\n")
    cur.close()
    conn.close()


def most_error_requests():
    conn = psycopg2.connect(dbname='news')
    cur = conn.cursor()
    art = """SELECT status_fail.day AS Datee,
    round((status_fail.num_NotFound*100.00/status_log.num_log) ,2) as Error
    FROM status_fail , status_log
    WHERE status_fail.day = status_log.day
    AND status_fail.num_NotFound >= 1000
    ORDER BY Error DESC;"""
    cur.execute(art)
    print("Days Did More Than 1% Of Requests Lead To Errors:", cur.rowcount)
    data = cur.fetchall()

    for row in data:
        p = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
        print('"{:%B %d, %Y}" -- {}% Errors'.format(p, row[1]))

    cur.close()
    conn.close()


if __name__ == '__main__':
    popular_three_articles()
    most_popular_authors()
    most_error_requests()

