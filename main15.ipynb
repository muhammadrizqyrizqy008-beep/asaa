# ==========================================================
# TUGAS PRAKTIKUM 3
# MULTIPROCESSING PYTHON
#
# No 1 : Analisis Speedup Skala Multiprocessing
# No 2 : Shared Memory vs Message Passing
# No 3 : Producer Consumer Antar-Proses
# No 4 : Refleksi
#
# Dibuat untuk VS Code Windows
# ==========================================================


import multiprocessing as mp
import time
import matplotlib.pyplot as plt



# ==========================================================
# NO 1
# ANALISIS SPEEDUP SKALA MULTIPROCESSING
# ==========================================================

"""
Tujuan:
Melakukan pengujian performa multiprocessing dengan
membandingkan metode sequential dan parallel.

Beban kerja yang digunakan adalah menghitung jumlah
bilangan prima menggunakan fungsi hitung_prima().

Pengujian dilakukan dengan jumlah worker:
1, 2, 4, dan 8.

Speedup dihitung dengan rumus:

Speedup = Waktu Sequential / Waktu Parallel
"""


def hitung_prima(n):

    jumlah = 0


    for angka in range(2, n):

        prima = True


        for i in range(2, int(angka**0.5)+1):

            if angka % i == 0:

                prima = False
                break


        if prima:

            jumlah += 1


    return jumlah




def no1_speedup():


    print("\n==============================")
    print("NO 1 - ANALISIS SPEEDUP")
    print("==============================")


    # Data pekerjaan

    daftar_n = [
        80000,
        80000,
        80000,
        80000
    ]



    # --------------------------
    # Sequential
    # --------------------------

    mulai = time.perf_counter()


    hasil_seq = []

    for n in daftar_n:

        hasil_seq.append(
            hitung_prima(n)
        )


    waktu_seq = time.perf_counter()-mulai



    print("\nSequential")

    print("Hasil :", hasil_seq)

    print(
        "Waktu :",
        round(waktu_seq,4),
        "detik"
    )



    # --------------------------
    # Multiprocessing
    # --------------------------


    worker_list = [
        1,
        2,
        4,
        8
    ]


    speedup = []



    for worker in worker_list:


        mulai = time.perf_counter()



        # Pool membagi pekerjaan ke beberapa proses

        with mp.Pool(
            processes=worker
        ) as pool:


            hasil = pool.map(
                hitung_prima,
                daftar_n
            )



        waktu = time.perf_counter()-mulai



        sp = waktu_seq / waktu


        speedup.append(sp)



        print("\nWorker :",worker)

        print(
            "Hasil :",
            hasil
        )

        print(
            "Waktu :",
            round(waktu,4),
            "detik"
        )


        print(
            "Speedup :",
            round(sp,2)
        )



    # Grafik

    plt.figure(figsize=(7,4))


    plt.plot(
        worker_list,
        speedup,
        marker="o",
        label="Speedup Aktual"
    )


    plt.plot(
        worker_list,
        worker_list,
        linestyle="--",
        label="Ideal"
    )


    plt.xlabel(
        "Jumlah Worker"
    )

    plt.ylabel(
        "Speedup"
    )


    plt.title(
        "Speedup Multiprocessing"
    )


    plt.legend()

    plt.grid()


    plt.show()





# ==========================================================
# NO 2
# SHARED MEMORY VS MESSAGE PASSING
# ==========================================================


"""
Queue:
Menggunakan metode Message Passing.

Setiap proses bekerja sendiri kemudian mengirimkan
hasil melalui Queue.


Value:
Menggunakan Shared Memory.

Beberapa proses mengakses data yang sama sehingga
membutuhkan Lock agar tidak terjadi race condition.
"""



def proses_queue(q):


    total = 0


    for i in range(1000000):

        total += 1



    q.put(total)




def no2_queue():


    print("\n==============================")
    print("NO 2 - QUEUE")
    print("==============================")


    q = mp.Queue()


    proses=[]


    mulai=time.perf_counter()



    for i in range(4):


        p = mp.Process(
            target=proses_queue,
            args=(q,)
        )


        p.start()

        proses.append(p)




    hasil=0



    for p in proses:

        hasil += q.get()



    for p in proses:

        p.join()



    waktu=time.perf_counter()-mulai



    print(
        "Hasil Queue :",
        hasil
    )


    print(
        "Waktu :",
        round(waktu,4),
        "detik"
    )






def proses_value(data,lock):


    total=0



    for i in range(1000000):

        total+=1



    with lock:

        data.value += total





def no2_value():


    print("\n==============================")
    print("NO 2 - SHARED MEMORY VALUE")
    print("==============================")


    data = mp.Value(
        'i',
        0
    )


    lock = mp.Lock()


    proses=[]


    mulai=time.perf_counter()



    for i in range(4):


        p = mp.Process(
            target=proses_value,
            args=(data,lock)
        )


        p.start()

        proses.append(p)



    for p in proses:

        p.join()



    waktu=time.perf_counter()-mulai



    print(
        "Hasil Value :",
        data.value
    )


    print(
        "Waktu :",
        round(waktu,4),
        "detik"
    )






# ==========================================================
# NO 3
# PRODUCER CONSUMER
# ==========================================================


"""
Producer bertugas menghasilkan data.

Consumer mengambil data dari Queue dan memprosesnya.

Queue digunakan sebagai media komunikasi antar proses.
"""



def producer(q):


    for i in range(10):

        q.put(i)



    q.put(None)






def consumer(q):


    while True:


        data=q.get()



        if data is None:

            break



        print(
            "Consumer menerima:",
            data
        )






def no3_producer_consumer():


    print("\n==============================")
    print("NO 3 - PRODUCER CONSUMER")
    print("==============================")


    q=mp.Queue()



    p1=mp.Process(
        target=producer,
        args=(q,)
    )


    p2=mp.Process(
        target=consumer,
        args=(q,)
    )



    p1.start()

    p2.start()



    p1.join()

    p2.join()





# ==========================================================
# NO 4
# REFLEKSI
# ==========================================================


"""
Manager digunakan ketika membutuhkan struktur data
yang lebih kompleks seperti list dan dictionary.

Value dan Array menggunakan shared memory langsung
sehingga lebih cepat untuk data sederhana.

Manager memiliki kelebihan fleksibilitas,
tetapi memiliki overhead komunikasi lebih besar.

Untuk perhitungan numerik sederhana,
Value atau Array lebih efisien.

Untuk aplikasi dengan struktur data kompleks,
Manager lebih mudah digunakan.
"""



def no4_refleksi():


    print("\n==============================")
    print("NO 4 - REFLEKSI")
    print("==============================")


    print(
    """
Manager digunakan untuk berbagi data kompleks
antar proses.

Value dan Array cocok untuk data sederhana
karena menggunakan shared memory.

Pemilihan metode tergantung kebutuhan:
- Kecepatan tinggi -> Value/Array
- Fleksibilitas data -> Manager
    """
    )





# ==========================================================
# MAIN PROGRAM
# ==========================================================


if __name__ == "__main__":


    no1_speedup()


    no2_queue()


    no2_value()


    no3_producer_consumer()


    no4_refleksi()