#!/usr/bin/python3
import gi
#Gtk 3 import
gi.require_version("Gtk","3.0")
from gi.repository import Gtk


class Eliquid():
    def __init__(self,menge,aroma,staerke,shots_staerke):
        self.menge = menge
        self.aroma = aroma
        self.staerke = staerke
        self.shots_staerke = shots_staerke
        self.aroma_fertig = (self.menge / 100) * self.aroma
        self.shots_menge = (self.menge / self.shots_staerke) * self.staerke
        i = self.shots_staerke - self.staerke
        self.base = self.menge / self.shots_staerke * i
        self.base = self.base - self.aroma_fertig


def berechne():
    menge = int(builder.get_object("entry_menge").get_text())
    aroma = int(builder.get_object("entry_aroma").get_text())
    staerke = int(builder.get_object("entry_staerke").get_text())
    shots_staerke = int(builder.get_object("cmb_staerke").get_active_text())

    eliquid = Eliquid(menge,aroma,staerke,shots_staerke)
    
    builder.get_object("label_aromafertig").set_text("%.1f"%eliquid.aroma_fertig)
    builder.get_object("label_shotsfertig").set_text("%.1f"%eliquid.shots_menge)
    builder.get_object("label_basefertig").set_text("%.1f"%eliquid.shots_menge)

class Handler:
    def on_window_main_destroy(self,*args):
        Gtk.main_quit()

    def on_button_berechnen_clicked(self,*args):
        berechne()

    def on_button_fertig_clicked(self,*args):     
        Gtk.main_quit()

    def on_btn_clear_clicked(self,*args):
        builder.get_object("entry_menge").set_text("")
        builder.get_object("entry_aroma").set_text("")
        builder.get_object("entry_staerke").set_text("")
        builder.get_object("label_aromafertig").set_text("")
        builder.get_object("label_shotsfertig").set_text("")
        builder.get_object("label_basefertig").set_text("")


builder = Gtk.Builder()
builder.add_from_file(r"eLiquid.glade")
builder.connect_signals(Handler())
window = builder.get_object("window_main")
window.show_all()
Gtk.main()
