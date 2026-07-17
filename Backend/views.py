from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import db

# ==================== CUSTOMER VIEWS ====================
@api_view(['POST'])
def add_customer(request):
    try:
        new_id = db.add_customer(request.data)
        target_id = request.data.get('customer_id', new_id)
        created_customer = db.get_customer_by_id(target_id)
        return Response(created_customer, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_customers(request):
    try:
        customers = db.get_customers()
        return Response(customers, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_customer(request, id):
    try:
        exists = db.get_customer_by_id(id)
        if not exists:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        updated = db.update_customer(id, request.data)
        return Response(updated, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        exists = db.get_customer_by_id(id)
        if not exists:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        db.delete_customer(id)
        return Response({"message": "Customer deleted successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==================== ISLAND VIEWS ====================
@api_view(['POST'])
def add_island(request):
    try:
        new_id = db.add_island(request.data)
        target_id = request.data.get('island_id', new_id)
        created_island = db.get_island_by_id(target_id)
        return Response(created_island, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_islands(request):
    try:
        islands = db.get_islands()
        return Response(islands, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_island(request, id):
    try:
        exists = db.get_island_by_id(id)
        if not exists:
            return Response({"error": "Island not found"}, status=status.HTTP_404_NOT_FOUND)
        updated = db.update_island(id, request.data)
        return Response(updated, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_island(request, id):
    try:
        exists = db.get_island_by_id(id)
        if not exists:
            return Response({"error": "Island not found"}, status=status.HTTP_404_NOT_FOUND)
        db.delete_island(id)
        return Response({"message": "Island deleted successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==================== RESORT & PACKAGE VIEWS ====================
@api_view(['POST'])
def add_package(request):
    try:
        new_id = db.add_package(request.data)
        target_id = request.data.get('package_id', new_id)
        created_package = db.get_package_by_id(target_id)
        return Response(created_package, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_packages(request):
    try:
        packages = db.get_packages()
        return Response(packages, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_package(request, id):
    try:
        exists = db.get_package_by_id(id)
        if not exists:
            return Response({"error": "Package not found"}, status=status.HTTP_404_NOT_FOUND)
        updated = db.update_package(id, request.data)
        return Response(updated, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_package(request, id):
    try:
        exists = db.get_package_by_id(id)
        if not exists:
            return Response({"error": "Package not found"}, status=status.HTTP_404_NOT_FOUND)
        db.delete_package(id)
        return Response({"message": "Package deleted successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==================== BOOKING VIEWS ====================
@api_view(['POST'])
def add_booking(request):
    try:
        new_id = db.add_booking(request.data)
        target_id = request.data.get('booking_id', new_id)
        created_booking = db.get_booking_by_id(target_id)
        return Response(created_booking, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_bookings(request):
    try:
        bookings = db.get_bookings()
        return Response(bookings, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_booking(request, id):
    try:
        exists = db.get_booking_by_id(id)
        if not exists:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
        updated = db.update_booking(id, request.data)
        return Response(updated, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_booking(request, id):
    try:
        exists = db.get_booking_by_id(id)
        if not exists:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
        db.delete_booking(id)
        return Response({"message": "Booking deleted successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==================== PAYMENT VIEWS ====================
@api_view(['POST'])
def add_payment(request):
    try:
        new_id = db.add_payment(request.data)
        target_id = request.data.get('payment_id', new_id)
        created_payment = db.get_payment_by_id(target_id)
        return Response(created_payment, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_payments(request):
    try:
        payments = db.get_payments()
        return Response(payments, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_payment(request, id):
    try:
        exists = db.get_payment_by_id(id)
        if not exists:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        updated = db.update_payment(id, request.data)
        return Response(updated, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_payment(request, id):
    try:
        exists = db.get_payment_by_id(id)
        if not exists:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        db.delete_payment(id)
        return Response({"message": "Payment deleted successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
