from django.db import connection
from django.shortcuts import render


def view_reports(request):
    """Функция отображения меню reports."""
    return render(request, "reports_menu.html")


def report1(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM book;")
        count_of_book = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM client;")
        count_of_clients = cursor.fetchall()
    data = [count_of_book, count_of_clients]

    return render(
        request,
        "report.html",
        {"data": data, "title": "Количество книг и количество читателей"}
    )


def report2(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT client.client_name, count(book_info.book_id_id) as book_count FROM client
            INNER JOIN book_info ON client.id = book_info.client_id_id GROUP BY client_name;""")
        data = cursor.fetchall()

    return render(
        request,
        "report.html",
        {"data": data, "title": "Количество книг, которые брал каждый читатель за все время"}
    )


def report3(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT book.title, count(book_info.book_id_id) as book_count FROM book
            INNER JOIN book_info ON book.id = book_info.book_id_id AND book_info.return_date is NULL 
            GROUP BY title;""")
        data = cursor.fetchall()

    return render(
        request,
        "report.html",
        {"data": data, "title": "Количество книг, которые сейчас находится на руках у каждого читателя"}
    )


def report4(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT client_name, TO_CHAR(visit_date, 'YYYY-MM-DD') FROM client;""")
        data = cursor.fetchall()

    return render(
        request,
        "report.html",
        {"data": data, "title": "Дата последнего посещения читателем библиотеки"}
    )


def report5(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT book.author, count(book_info.book_id_id) as book_count FROM book
            INNER JOIN book_info ON book.id = book_info.book_id_id AND book_info.return_date is NULL 
            GROUP BY author ORDER BY book_count DESC LIMIT 1;""")
        data = cursor.fetchall()

    return render(
        request,
        "report.html",
        {"data": data, "title": "Самый читаемый автор"}
    )


def report6(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT book.genre FROM book
            INNER JOIN book_info ON book.id = book_info.book_id_id AND book_info.return_date is NULL 
            GROUP BY genre ORDER BY count(book_info.book_id_id) DESC;""")
        data = cursor.fetchall()

    return render(
        request,
        "report.html",
        {"data": data, "title": "Самый предпочитаемые читателями жанры по убыванию"}
    )


def report7(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT client_name, main_client.id,
            
             (
                SELECT genre FROM book
                INNER JOIN book_info ON book.id = book_info.book_id_id
                INNER JOIN client as second_client ON second_client.id = book_info.client_id_id
                WHERE second_client.id = main_client.id
                GROUP BY genre ORDER BY count(genre) DESC LIMIT 1
             )
           
            FROM client as main_client
            INNER JOIN book_info ON main_client.id = book_info.client_id_id
            INNER JOIN book ON book.id = book_info.book_id_id
            GROUP BY client_name, main_client.id;"""
        )
        data = cursor.fetchall()

    return render(
        request,
        "report.html",
        {"data": data, "title": "Любимый жанр каждого читателя"}
    )
