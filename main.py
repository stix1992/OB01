from classes import store as st
from classes import task as ts

print('\nМенеджер задач:')

tasks = ts.Task()

tasks.add_task("Проснуться", "2024-06-10 08:00:00")
tasks.add_task("Умыться", "2024-06-10 09:00:00")
tasks.add_task("Поесть", "2024-06-10 10:00:00")
print(tasks)
tasks.mark_completed("Проснуться")
tasks.mark_completed("Поработать")
print(tasks)

print('\nСеть магазинов:')

store1 = st.Store("Магазин 1", "123 Главная улица")
store2 = st.Store("Магазин 2", "456 Улица Вязов")
store3 = st.Store("Магазин 3", "789 Кленовая улица")

# Добавление товаров в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store2.add_item("апельсины", 0.6)
store2.add_item("груши", 0.8)
store3.add_item("виноград", 2.0)
store3.add_item("лимоны", 1.0)

print(store1)

# Добавление товара
store1.add_item("вишни", 3.0)
print("После добавления вишен:")
print(store1)

# Обновление цены
store1.update_price("бананы", 0.85)
print("После обновления цены на бананы:")
print(store1)

# Удаление товара
store1.remove_item("яблоки")
print("После удаления яблок:")
print(store1)

# Запрос цены
print(f"Цена на бананы: {store1.get_price('бананы')}")
print(f"Цена на яблоки: {store1.get_price('яблоки')}")



