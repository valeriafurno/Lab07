import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_biblioteche(self):
        biblioteche = self._model.get_biblioteche()

        self._view.dropdown_biblioteca.options.append(
            ft.dropdown.Option(key="", text="Nessun filtro"))

        if biblioteche is not None:
            for biblioteca in biblioteche:
                self._view.dropdown_biblioteca.options.append(
                    ft.dropdown.Option(key=str(biblioteca.id), text=biblioteca.nome)
                )
        else:
            self._view.show_alert("Errore nel caricamento delle biblioteche!")

        self._view.update()

    def popola_dropdown_generi(self):
        generi = self._model.get_generi()

        self._view.dropdown_genere.options.append(
            ft.dropdown.Option(key="", text="Nessun filtro")
            )
        if generi is not None:
            for genere in generi:
                self._view.dropdown_genere.options.append(
                    ft.dropdown.Option(key=genere, text=genere)
                )
        else:
            self._view.show_alert("Errore nel caricamento dei generi!")
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def seleziona_biblioteca(self, e):
        if e.control.value == "":
            self.biblioteca_selezionata = ""
        else:
            self.biblioteca_selezionata = int(e.control.value)

    def seleziona_genere(self, e):
        if e.control.value == "":
            self.genere_selezionato = ""
        else:
            self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):
        if self.biblioteca_selezionata is None and self.genere_selezionato is None:
            self._view.show_alert("!! Inserire almeno un filtro !!")
            return
        #recupero i valori selezionati nei Dropdown
        biblioteca= self.biblioteca_selezionata
        genere = self.genere_selezionato

        #converto i valori "" in None, perchè COALESCE nella query SQL utilizza NULL
        # per indicare che il relativo filtro non deve essere applicato.
        if biblioteca == "":
            biblioteca =  None
        if genere == "":
            genere= None

        self._view.lista_libri.controls.clear()
        libri= self._model.get_libri_filtrati((biblioteca),(genere))
        if libri is not None:
            if len(libri)> 0:
                for libro in libri:
                    self._view.lista_libri.controls.append(ft.Text(f"{libro}"))
                self._view.update()
            else:
                self._view.show_alert("Nessun Libro Trovato")
        else:
            self._view.show_alert("non è stato possibile connettersi al database")
