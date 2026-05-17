




<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Available Trucks - Truck Booking</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #eef1f4;
      margin: 0;
      padding: 0;
    }

    .header {
      background-color: #007bff;
      color: white;
      text-align: center;
      padding: 20px;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 30px;
    }

    .truck-card {
      background-color: white;
      width: 90%;
      max-width: 600px;
      padding: 20px;
      margin: 15px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .truck-card h3 {
      margin-top: 0;
    }

    .truck-details {
      margin-bottom: 15px;
    }

    .buttons {
      display: flex;
      gap: 10px;
    }

    .btn {
      padding: 10px 15px;
      font-size: 14px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      color: white;
      transition: 0.3s;
    }

    .btn-book {
      background-color: #28a745;
    }

    .btn-book:hover {
      background-color: #218838;
    }

    .btn-contact {
      background-color: #17a2b8;
    }

    .btn-contact:hover {
      background-color: #138496;
    }
  </style>
</head>
<body>

  <div class="header">
    <h1>Available Trucks</h1>
  </div>

  <div class="container" id="truckList">
    <!-- Firebase data will populate here -->
  </div>

  <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore-compat.js"></script>

  <script>
    const firebaseConfig = {
      apiKey: "AIzaSyCuhbxnhqUZnbfYELDHTCJEI1k-LP1eKBo",
      authDomain: "truckbooking-ab4d0.firebaseapp.com",
      projectId: "truckbooking-ab4d0",
      storageBucket: "truckbooking-ab4d0.appspot.com",
      messagingSenderId: "249339346525",
      appId: "1:249339346525:web:c3f2a1ce605eeccb2357b4"
    };

    firebase.initializeApp(firebaseConfig);
    const db = firebase.firestore();

    const truckListDiv = document.getElementById('truckList');

    db.collection("trucks").get().then(snapshot => {
      snapshot.forEach(doc => {
        const truck = doc.data();

        const card = document.createElement('div');
        card.className = 'truck-card';

        card.innerHTML = `
          <h3>${truck.truckName} (${truck.truckCategory})</h3>
          <div class="truck-details">
            <p><strong>Vehicle Number:</strong> ${truck.vehicleNumber}</p>
            <p><strong>Capacity:</strong> ${truck.truckCapacity} tons</p>
            <p><strong>Company:</strong> ${truck.truckCompany}</p>
            <p><strong>Driver Name:</strong> ${truck.driverName}</p>
            <p><strong>Driver Contact:</strong> ${truck.driverContact}</p>
            <p><strong>Available:</strong> ${truck.available ? "Yes" : "No"}</p>
          </div>
          <div class="buttons">
            <button class="btn btn-book" onclick="bookTruck('${truck.truckName}')">Book Truck</button>
            <button class="btn btn-contact" onclick="window.location.href='contact.html'">Contact</button>
          </div>
        `;

        truckListDiv.appendChild(card);
      });
    }).catch(err => {
      console.error("Error fetching trucks:", err);
      truckListDiv.innerHTML = "<p>Error loading trucks.</p>";
    });

    function bookTruck(truckName) {
      alert(`Redirecting to booking for ${truckName}`);
      window.location.href = 'booking.html';
    }
  </script>

</body>
</html>


































import requests

def get_weather(city_name, api_key):
    # Set units to 'metric' for Celsius or 'imperial' for Fahrenheit
    url = f"http://openweathermap.org{city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {desc.capitalize()}")
    else:
        print("Error: Could not find city or API key is invalid.")

# Replace with your actual API key from OpenWeatherMap
MY_API_KEY = "your_api_key_here"
city = input("Enter city name: ")
get_weather(city, MY_API_KEY)























import requests

def get_weather(city_name, api_key):
    # Set units to 'metric' for Celsius or 'imperial' for Fahrenheit
    url = f"http://openweathermap.org{city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {desc.capitalize()}")
    else:
        print("Error: Could not find city or API key is invalid.")

# Replace with your actual API key from OpenWeatherMap
MY_API_KEY = "your_api_key_here"
city = input("Enter city name: ")
get_weather(city, MY_API_KEY)














