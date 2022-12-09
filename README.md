# isai-project-2022
Kedaireka Project Log Book 

project start 6 September 2022
target finish 11 Desember 2022

6 September - 6 November:
	Pengambilan Sample data
	Pembelajaran mandiri dari internet
	UT dengan petani Klaten
	Menunggu data keluar dari lab untuk memulai pengerjaan model ML

6 November:
	Project Manager (Mas Satno) masuk dan mulai menangani project ini 

7 November:
	Memulai magang dengan kantor Beehive secara hybrid, data karbon dari HST 0 padi sudah turun

8 November - 13 November:
	Memulai diskusi dan pengerjaan feature extraction dari data yang sudah tersedia

14 November - 16 November:
	Mengeksplor metode resize yang mungkin dapat digunakan untuk rescaling data citra, untuk memperkecil
	fitur yang nantinya akan digunakan dalam training model
	Mencoba menyiapkan model sambil menunggu data

17 November:
	Diskusi dgn pak Kun, memperbaiki program image processing, tapi baru dengan 1 metode scaling, 
	dengan interpolation, sudah bisa mendapat nilai" ndvi, ci, dsb dan dijadikan file csv
	sebenarnya model juga sudah jadi, tapi akurasinya sangat buruk, belum bisa eksplor untuk mencari metode yang tepat,
	karena datanya juga belum lengkap 

22 November:
	Tim beehive dan kedaireka memutuskan menggunakan data Nitrogen dari penelitian sebelumnya terlebih dahulu 
	untuk pembuatan model ML, karena hasil lab dari pengambilan data karbon belum selesai juga, dan dari statistik
	dibilang ada korelasi positif antara karbon, nitrogen dan fitur" yang digunakan seperti ndvi,ci, dll

23 November - 28 November:
	Membuat dataset nitrogen dari pengolahan citra lahan sawah, HST 0 tetap menggunakan data Klaten dan HST 1 - 2 menggunakan
	data Subang dari penelitian beehive sebelumnya
	Mengupdate model ML yang sudah dibuat sebelumnya dengan menggunakan dataset nilai Nitrogen

	Menghasilkan dua model untuk komoditas padi, yaitu model regresi untuk prediksi nilai karbon, dan model klasifikasi dengan target berupa HST

	Model regresi menggunakan dataset berjumlah 90 record terdiri dari masing-masing 30 record per data hst
	Model klasifikasi juga sama

	Algoritma yang digunakan untuk melakukan fit-train model ML kami semua masih menggunakan yang ada di library opensource
	Scikit-learn, decission tree regression untuk model regresi, menghasilkan model dengan 90% akurasi, masih ada kemungkinan overfit
	Kerass, sequential multi layer perceptron untuk yang model klasifikasi

1 Desember - 3 Desember:
	Membantu mendeploy model machine learning ke lambda untuk sedikit meringankan pembangunan pipeline aplikasi dari tim infra

6 Desember - 8 Desember:
	Data karbon dari Klaten sudah lengkap, memulai tahap pengolahan data dengan cropping data citra awal menjadi potongan - potongan 200x200 per titik
	Untuk memperbesar jumlah data, setiap titik yang seharusnya hanya menghasilkan 1 record digandakan menjadi 3 record dengan mengcrop 3 area disekitar titik,
	jadi ada 3 record dengan 1 nilai karbon yang sama jadi totalnya terdapat 270 record, tiap copy memiliki 3 HST, tiap hst terdapat 30 record

	Sebelumnya tiap entri data seharusnya memiliki 2 nilai karbon yaitu karbon tanaman dan tanah

	Dari update ini ternyata dari beehive mau nilai karbon dijadikan 1 saja dengan menjumlah nilai karbon tanah dan tanaman

	Mengupdate fungsi untuk preprocessing agar lebih mudah digunakan dengan data yang baru

	Setelah uji coba pembuatan model ML dengan menukarkan data set yang lama (nitrogen 90 entri campuran data klaten dan subang) dengan data baru (karbon 270 entri dari klaten)
	didapatkan hasil akurasi yang sangat kurang, hanya berkisar antara 0,08 - 0,3 untuk fungsi regressinya

	Setelah dilihat dari grafik data - data antar fitur tadi (ndvi, ci, ngrdi, gndvi) dengan nilai karbon total tidak menunjukan pola yang jelas

9 Desember:

	Melakukan penelitian ulang, untuk mengetes variabel apa yang menyebabkan akurasi menurun drastis, kemungkinan fungsi resize atau resolusi citra dari drone yang
	dari awal berbeda-beda




