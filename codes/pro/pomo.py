import gi
import subprocess

# Selecting the version and model
gi.require_version ('Gtk' , '3.0')

#import pygobject library
from gi.repository import Gtk , GLib , Gdk

# create window bar
class PomoBox (Gtk.Window):
    def __init__(self):
        super().__init__(title="Pomodoro")
        self.set_resizable(True)
        self.set_decorated(True)
        self.set_keep_above(True)

        self.work = 1 * 60
        self.rest = 1 * 60

        self.remaining = self.work
        self.is_work = True
        self.running = True
        self.cycle = 1

        bar = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=15
            )

        bar.set_margin_start(12)
        bar.set_margin_end(12)
        bar.set_margin_top(7)
        bar.set_margin_bottom(7)

        self.status = Gtk.Label(label="🟢 WORK")
        self.timer = Gtk.Label(label = "01:00")
        self.cycle_label = Gtk.Label(label = "round 1")
        self.stop_button = Gtk.Button(label = "stop")
        self.stop_button.connect("clicked", self.stop)
        self.skip_button = Gtk.Button(label = "skip")
        self.skip_button.connect("clicked", self.skip)

        bar.pack_start(
            self.status,
            False,
            False,
            0
        )
        bar.pack_start(
            self.cycle_label,
            False,
            False,
            0
                )
        bar.pack_start(
            self.timer,
            False,
            False,
            0
                )
        bar.pack_end(
            self.skip_button,
            False,
            False,
            0
                )
        bar.pack_end(
            self.stop_button,
            False,
            False,
            0
                )

        self.add(bar)
        GLib.timeout_add(1000,self.update)
    def update (self):

        if not self.running:
            return True
        self.remaining -= 1
        self.time()
        if self.remaining <= 0 :
            self.switch()

        return True

    def time (self):

        min = self.remaining // 60
        sec = self.remaining % 60

        self.timer.set_text(
            f"{min:02d}:{sec:02d}"
        )
        self.cycle_label.set_text(
            f"cycle {self.cycle}"
        )

        if self.is_work:
            self.status.set_text("🟢 WORK")
        else: 
            self.status.set_text("🔴 REST")

    def switch (self):
        subprocess.Popen(["notify-send", "Pomodoro" , "!!!! End Time !!!!"])

        if self.is_work:

            self.is_work = False
            self.remaining = self.rest
            

        else:
            self.is_work = True
            self.remaining = self.work
            self.cycle += 1

        self.time()
        print("\a", end="", flush=True)

    def stop(self,button):
        self.running = not self.running

        if self.running:

            self.stop_button.set_label("stop")
        else:

            self.stop_button.set_label("start")

    def skip (self , button):
        self.switch()


#   for running
window = PomoBox()

window.connect(
    "destroy",
    Gtk.main_quit
)

window.show_all()

Gtk.main()