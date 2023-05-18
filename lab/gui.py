import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, area, cost, size):
        self._area = area
        self._cost = cost
        self._size = size
    
    @property
    def area(self):
        return self._area
    
    @property
    def cost(self):
        return self._cost
    
    @property
    def size(self):
        return self._size

    @abstractmethod
    def calculate_quantity(self):
        pass
    
    @abstractmethod
    def calculate_cost(self):
        pass

class Wallpaper(Material):
    def __init__(self, area, cost, size):
        super().__init__(area, cost, size)
        self.name = "Обои"

    def calculate_quantity(self):
        size_parts = self.size.split("x")
        width = float(size_parts[0].strip())
        height = float(size_parts[1].strip())
        return self.area / (width * height)

    def calculate_cost(self):
        return self.calculate_quantity() * self.cost

    def __str__(self):
        return f"Материал: {self.name}, Площадь: {self.area}, Размер: {self.size}, Стоимость: {self.cost}"

class Tile(Material):
    def __init__(self, area, cost, size):
        super().__init__(area, cost, size)
        self.name = "Плитка"

    def calculate_quantity(self):
        size_parts = self.size.split("x")
        width = float(size_parts[0].strip())
        height = float(size_parts[1].strip())
        return self.area / (width * height)

    def calculate_cost(self):
        return self.calculate_quantity() * self.cost

    def __str__(self):
        return f"Материал: {self.name}, Площадь: {self.area}, Размер: {self.size}, Стоимость: {self.cost}"

class Laminate(Material):
    def __init__(self, area, cost, size):
        super().__init__(area, cost, size)
        self.name = "Ламинат"

    def calculate_quantity(self):
        size_parts = self.size.split("x")
        width = float(size_parts[0].strip())
        height = float(size_parts[1].strip())
        return self.area / (width * height)

    def calculate_cost(self):
        return self.calculate_quantity() * self.cost

    def __str__(self):
        return f"Материал: {self.name}, Площадь: {self.area}, Размер: {self.size}, Стоимость: {self.cost}"

class GUIWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Отделочные материалы")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.combo = Gtk.ComboBoxText()
        self.combo.insert(0, "1", "Обои")
        self.combo.insert(1, "2", "Плитка")
        self.combo.insert(2, "3", "Ламинат")
        self.combo.connect("changed", self.on_combo_changed)
        self.box.pack_start(self.combo, True, True, 0)

        self.label = Gtk.Label()
        self.box.pack_start(self.label, True, True, 0)

        self.entry_area = Gtk.Entry()
        self.entry_area.set_placeholder_text("Введите площадь, м^2")
        self.box.pack_start(self.entry_area, True, True, 0)

        self.entry_cost = Gtk.Entry()
        self.entry_cost.set_placeholder_text("Введите стоимость")
        self.box.pack_start(self.entry_cost, True, True, 0)

        self.entry_size = Gtk.Entry()
        self.entry_size.set_placeholder_text("Введите размеры")
        self.box.pack_start(self.entry_size, True, True, 0)

        self.button = Gtk.Button(label="Рассчитать")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_combo_changed(self, combo):
        material_id = self.combo.get_active_id()
        if material_id == "1":
            self.entry_size.set_placeholder_text("Введите размеры обоев(см)")
        elif material_id == "2":
            self.entry_size.set_placeholder_text("Введите размеры плитки(см)")
        elif material_id == "3":
            self.entry_size.set_placeholder_text("Введите размеры ламината(см)")

    def on_button_clicked(self, button):
        material_id = self.combo.get_active_id()
        area = float(self.entry_area.get_text())
        cost = float(self.entry_cost.get_text())
        size = self.entry_size.get_text()

        if material_id == "1":
            material = Wallpaper(area, cost, size)
        elif material_id == "2":
            material = Tile(area, cost, size)
        elif material_id == "3":
            material = Laminate(area, cost, size)

        quantity = material.calculate_quantity()
        total_cost = material.calculate_cost()

        self.label.set_text(f"Количество: {quantity}, Общая стоимость: {total_cost}")
        print(material)

win = GUIWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
