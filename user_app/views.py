from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from user_app.stringify import create_table_stringfy, create_relational_query
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import connection

# Create your views here.
@api_view(['GET'])

def viewUser(request):
    # content = {'message': 'Hello, World!'}
    query = f"""SELECT * FROM public."user"
                ORDER BY id ASC """

    with connection.cursor() as cursor:
        q_data = cursor.execute(query)
        q_data_fatch_all = cursor.fetchall()

        return Response(
            {
                "status": "success",
                "message": "Table created successfully",
                "data": q_data_fatch_all,
            },
            status=status.HTTP_200_OK,
        )

    



@api_view(["POST"])
def createTable(request):
    query_from_json = create_table_stringfy(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "Table created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


@api_view(["POST"])
def createUser(request):
    query_from_json = create_relational_query(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "User created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


@api_view(["POST"])
def createUserPost(request):
    query_from_json = create_relational_query(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "User post created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


@api_view(["POST"])
def createUserExperience(request):
    query_from_json = create_relational_query(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "User Experience Created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


@api_view(["POST"])
def createUserFollow(request):
    query_from_json = create_relational_query(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "User Follow Created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


@api_view(["POST"])
def createUserFriend(request):
    query_from_json = create_relational_query(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "User Friend Created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


@api_view(["POST"])
def createUserLike(request):
    query_from_json = create_relational_query(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "User Like Created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


@api_view(["POST"])
def createUserComment(request):
    query_from_json = create_relational_query(request.data)

    with connection.cursor() as cursor:

        try:
            cursor.execute(query_from_json)

            return Response(
                {
                    "status": "success",
                    "message": "User Comment Created successfully",
                    "data": request.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            err_msg = str(e)
            return Response(
                {
                    "status": "fail",
                    "message": err_msg,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )
