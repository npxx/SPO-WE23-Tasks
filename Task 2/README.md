# Task 2

- [x] Written a GET request in python using Django
- [x] Displayed the data in tabular form (The fetched data further contained api endpoints of residents and films; fetched names and titles for those respectively)
- [x] Added cache support using Django's inbuilt cached-page functionality
- [x] Added cache support using localStorage (and a custom expiration logic, too); (Django support disabled, can be re-enabled again)

`views.py`

```python
def data(request):
    url = 'https://swapi.dev/api/planets/1/'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        residents = []
        for resident_url in data['residents']:
            resident_response = requests.get(resident_url)
            if resident_response.status_code == 200:
                resident_data = resident_response.json()
                residents.append(resident_data['name'])

        films = []
        for film_url in data['films']:
            film_response = requests.get(film_url)
            if film_response.status_code == 200:
                film_data = film_response.json()
                films.append(film_data['title'])

        del data['residents']
        del data['films']
        html = render_to_string('table.html', {'data': data, 'residents': residents, 'films': films})  
        response = HttpResponse(html, content_type='text/html')
        response['Cache-Control'] = 'public, max-age=20'  
        return response
        # return render(request, 'table.html', {'data': data, 'residents': residents, 'films': films})
    else:
        return render(request, 'table.html', {'data': None,'residents': None})
```

Cache logic
```javascript
 function fetchAndCacheHTML() {
        var cachedHTML = localStorage.getItem("cachedHTML");

        if (cachedHTML) {
          document.getElementById("data-container").innerHTML = cachedHTML;
        } else {
          fetch("/data/", {
            headers: {
              "Cache-Control": "max-age=20",
            },
          })
            .then(function (response) {
              return response.text();
            })
            .then(function (data) {
              localStorage.setItem("cachedHTML", data);
              document.getElementById("data-container").innerHTML = data;

              setTimeout(function () {
                localStorage.removeItem("cachedHTML");
              }, 20 * 1000);
            })
            .catch(function (error) {
              console.log("Error:", error);
            });
        }
      }
```



| '/' | `/data/` (after GET) | `/cached/` |
| ---- | ---- | ---- |
|![image](https://github.com/npxx/SPO-WE23-Tasks/assets/96121824/56a6734e-d8b2-4231-98a2-5269aea5c629)|![image](https://github.com/npxx/SPO-WE23-Tasks/assets/96121824/80acf34b-4805-46d0-a6a8-84e6138c5012)|![image](https://github.com/npxx/SPO-WE23-Tasks/assets/96121824/98e04abb-caa1-42e7-b908-5623da60df7c)|

`cached` page becomes blank once we reload it after cache expires; it fetches the new data automatically and displays, caches it again
