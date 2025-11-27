# ===============================
# StudentNoteApp (One File Version)
# Menggunakan: page, variabel, if, module (class), looping, function
# ===============================

# --- MODULE buatan (menggunakan class sebagai modul) ---
class NotesModule:
    def __init__(self):
        self.notes = []  # variabel untuk menyimpan catatan

    def add_note(self):
        note = input("Masukkan catatan baru: ")
        self.notes.append(note)
        print("Catatan berhasil ditambahkan!\n")

    def view_notes(self):
        if len(self.notes) == 0:
            print("Belum ada catatan.\n")
        else:
            print("\n=== Daftar Catatan ===")
            for i, note in enumerate(self.notes, start=1):  # LOOPING
                print(f"{i}. {note}")
            print()

    def delete_note(self):
        if len(self.notes) == 0:
            print("Tidak ada catatan untuk dihapus.\n")
            return
        
        self.view_notes()
        try:
            index = int(input("Pilih nomor catatan yang ingin dihapus: "))
            if 1 <= index <= len(self.notes):
                removed = self.notes.pop(index - 1)
                print(f"Catatan '{removed}' berhasil dihapus!\n")
            else:
                print("Nomor tidak valid.\n")
        except:
            print("Input harus berupa angka.\n")


# --- PAGE: tampilan menu ---
def tampilkan_menu():
    print("""
===== StudentNoteApp =====
1. Tambah Catatan
2. Lihat Catatan
3. Hapus Catatan
4. Keluar
==========================
    """)

# --- FUNCTION utama ---
def main():
    notes_module = NotesModule()  # module dalam bentuk class

    while True:   # LOOPING menu
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4): ")

        # LOGIKA IF
        if pilihan == "1":
            notes_module.add_note()
        elif pilihan == "2":
            notes_module.view_notes()
        elif pilihan == "3":
            notes_module.delete_note()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan StudentNoteApp!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")


# --- menjalankan program ---
if __name__ == "__main__":
    main()
