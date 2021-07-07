# MapSpeculatr
Obrazy poszczególnych mikroserwisów (maps, front, game_server i users) są zbudowane przez dockera za pomocą odpowiednich poleceń, np. docker build -t szumiel/maps .

Te obrazy są później przesyłane na dockerhuba(przez docker desktop).

Na platformie cloud z tych mikroserwisów robimy 4 workloady i stawiamy serwery djangowe.

Dla maps i users stawiamy jeszcze workload z celery workerem na odpowiedniej kolejce, np. celery -A users worker -E -Q users

Oprócz tego mamy serwis rabbitmq utworzony w miarę automatycznie z marketplace'a i serwer mysql utworzony za pomocą helma przez konsolę z ręcznie dodanymi bazami dla odpowiednich mikroserwisów.
