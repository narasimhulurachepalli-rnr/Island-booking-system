import pymongo
import os

MONGO_URI = "mongodb+srv://rachepallinandini_db_user:Nandini2005@cluster0.dli41nw.mongodb.net/"
DB_NAME = "island_booking"

print("Initializing MongoDB Connection...")
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
customers_col = db["customers"]
islands_col = db["islands"]
packages_col = db["packages"]
bookings_col = db["bookings"]
payments_col = db["payments"]

def get_next_id(collection, id_field, start_from):
    """
    Finds the maximum integer ID value in the collection for a given id_field,
    and returns max_val + 1. If empty, returns start_from.
    """
    try:
        max_doc = collection.find_one(sort=[(id_field, -1)])
        if max_doc and id_field in max_doc:
            return int(max_doc[id_field]) + 1
    except Exception as e:
        print(f"Error generating next ID for {id_field}: {e}")
    return start_from

def serialize_doc(doc):
    if doc is None:
        return None
    doc = dict(doc)
    doc.pop("_id", None)
    return doc

# ==================== CUSTOMER CRUD ====================
def add_customer(data):
    customer_id = data.get('customer_id')
    if customer_id is None:
        customer_id = get_next_id(customers_col, 'customer_id', 101)
    else:
        customer_id = int(customer_id)
        
    if customers_col.find_one({"customer_id": customer_id}):
        raise Exception(f"Customer with ID {customer_id} already exists")

    doc = {
        "customer_id": customer_id,
        "full_name": data.get("full_name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "nationality": data.get("nationality"),
        "password": data.get("password")
    }
    customers_col.insert_one(doc)
    return customer_id

def get_customers():
    return [serialize_doc(doc) for doc in customers_col.find()]

def get_customer_by_id(customer_id):
    return serialize_doc(customers_col.find_one({"customer_id": int(customer_id)}))

def update_customer(customer_id, data):
    customers_col.update_one(
        {"customer_id": int(customer_id)},
        {"$set": {
            "full_name": data.get("full_name"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "nationality": data.get("nationality"),
            "password": data.get("password")
        }}
    )
    return get_customer_by_id(customer_id)

def delete_customer(customer_id):
    customers_col.delete_one({"customer_id": int(customer_id)})
    return True

# ==================== ISLAND CRUD ====================
def add_island(data):
    island_id = data.get('island_id')
    if island_id is None:
        island_id = get_next_id(islands_col, 'island_id', 201)
    else:
        island_id = int(island_id)
        
    if islands_col.find_one({"island_id": island_id}):
        raise Exception(f"Island with ID {island_id} already exists")

    doc = {
        "island_id": island_id,
        "island_name": data.get("island_name"),
        "country": data.get("country"),
        "description": data.get("description"),
        "climate": data.get("climate"),
        "best_season": data.get("best_season"),
        "image_url": data.get("image_url")
    }
    islands_col.insert_one(doc)
    return island_id

def get_islands():
    return [serialize_doc(doc) for doc in islands_col.find()]

def get_island_by_id(island_id):
    return serialize_doc(islands_col.find_one({"island_id": int(island_id)}))

def update_island(island_id, data):
    islands_col.update_one(
        {"island_id": int(island_id)},
        {"$set": {
            "island_name": data.get("island_name"),
            "country": data.get("country"),
            "description": data.get("description"),
            "climate": data.get("climate"),
            "best_season": data.get("best_season"),
            "image_url": data.get("image_url")
        }}
    )
    return get_island_by_id(island_id)

def delete_island(island_id):
    islands_col.delete_one({"island_id": int(island_id)})
    return True

# ==================== RESORT & PACKAGE CRUD ====================
def add_package(data):
    package_id = data.get('package_id')
    if package_id is None:
        package_id = get_next_id(packages_col, 'package_id', 301)
    else:
        package_id = int(package_id)
        
    if packages_col.find_one({"package_id": package_id}):
        raise Exception(f"Package with ID {package_id} already exists")

    doc = {
        "package_id": package_id,
        "island_name": data.get("island_name"),
        "resort_name": data.get("resort_name"),
        "package_name": data.get("package_name"),
        "duration": data.get("duration"),
        "price": float(data.get("price")) if data.get("price") is not None else 0.0,
        "included_services": data.get("included_services")
    }
    packages_col.insert_one(doc)
    return package_id

def get_packages():
    return [serialize_doc(doc) for doc in packages_col.find()]

def get_package_by_id(package_id):
    return serialize_doc(packages_col.find_one({"package_id": int(package_id)}))

def update_package(package_id, data):
    packages_col.update_one(
        {"package_id": int(package_id)},
        {"$set": {
            "island_name": data.get("island_name"),
            "resort_name": data.get("resort_name"),
            "package_name": data.get("package_name"),
            "duration": data.get("duration"),
            "price": float(data.get("price")) if data.get("price") is not None else 0.0,
            "included_services": data.get("included_services")
        }}
    )
    return get_package_by_id(package_id)

def delete_package(package_id):
    packages_col.delete_one({"package_id": int(package_id)})
    return True

# ==================== BOOKING CRUD ====================
def add_booking(data):
    booking_id = data.get('booking_id')
    if booking_id is None:
        booking_id = get_next_id(bookings_col, 'booking_id', 401)
    else:
        booking_id = int(booking_id)
        
    if bookings_col.find_one({"booking_id": booking_id}):
        raise Exception(f"Booking with ID {booking_id} already exists")

    doc = {
        "booking_id": booking_id,
        "customer_name": data.get("customer_name"),
        "island_name": data.get("island_name"),
        "package_name": data.get("package_name"),
        "travel_date": data.get("travel_date"),
        "number_of_people": int(data.get("number_of_people")) if data.get("number_of_people") is not None else 0,
        "total_amount": float(data.get("total_amount")) if data.get("total_amount") is not None else 0.0,
        "booking_status": data.get("booking_status", "Pending")
    }
    bookings_col.insert_one(doc)
    return booking_id

def get_bookings():
    return [serialize_doc(doc) for doc in bookings_col.find()]

def get_booking_by_id(booking_id):
    return serialize_doc(bookings_col.find_one({"booking_id": int(booking_id)}))

def update_booking(booking_id, data):
    bookings_col.update_one(
        {"booking_id": int(booking_id)},
        {"$set": {
            "customer_name": data.get("customer_name"),
            "island_name": data.get("island_name"),
            "package_name": data.get("package_name"),
            "travel_date": data.get("travel_date"),
            "number_of_people": int(data.get("number_of_people")) if data.get("number_of_people") is not None else 0,
            "total_amount": float(data.get("total_amount")) if data.get("total_amount") is not None else 0.0,
            "booking_status": data.get("booking_status")
        }}
    )
    return get_booking_by_id(booking_id)

def delete_booking(booking_id):
    bookings_col.delete_one({"booking_id": int(booking_id)})
    return True

# ==================== PAYMENT CRUD ====================
def add_payment(data):
    payment_id = data.get('payment_id')
    if payment_id is None:
        payment_id = get_next_id(payments_col, 'payment_id', 501)
    else:
        payment_id = int(payment_id)
        
    if payments_col.find_one({"payment_id": payment_id}):
        raise Exception(f"Payment with ID {payment_id} already exists")

    doc = {
        "payment_id": payment_id,
        "booking_id": int(data.get("booking_id")) if data.get("booking_id") is not None else 0,
        "customer_name": data.get("customer_name"),
        "amount": float(data.get("amount")) if data.get("amount") is not None else 0.0,
        "payment_method": data.get("payment_method"),
        "payment_status": data.get("payment_status", "Pending"),
        "transaction_id": data.get("transaction_id"),
        "payment_date": data.get("payment_date")
    }
    payments_col.insert_one(doc)
    return payment_id

def get_payments():
    return [serialize_doc(doc) for doc in payments_col.find()]

def get_payment_by_id(payment_id):
    return serialize_doc(payments_col.find_one({"payment_id": int(payment_id)}))

def update_payment(payment_id, data):
    payments_col.update_one(
        {"payment_id": int(payment_id)},
        {"$set": {
            "booking_id": int(data.get("booking_id")) if data.get("booking_id") is not None else 0,
            "customer_name": data.get("customer_name"),
            "amount": float(data.get("amount")) if data.get("amount") is not None else 0.0,
            "payment_method": data.get("payment_method"),
            "payment_status": data.get("payment_status"),
            "transaction_id": data.get("transaction_id"),
            "payment_date": data.get("payment_date")
        }}
    )
    return get_payment_by_id(payment_id)

def delete_payment(payment_id):
    payments_col.delete_one({"payment_id": int(payment_id)})
    return True
