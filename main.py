from autopy import mouse, key
from mouse_positions import MousePositions, Coordinates
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

wait_time = 0.3
long_wait_time = 4


def alt_tab():
    key.toggle(key.Code.ALT, True)
    time.sleep(wait_time)
    key.tap(key.Code.TAB)
    time.sleep(wait_time)
    key.toggle(key.Code.ALT, False)
    time.sleep(wait_time)
    print("Alt Tabbed")


def alt_double_tab():
    key.toggle(key.Code.ALT, True)
    time.sleep(wait_time)
    key.tap(key.Code.TAB)
    time.sleep(wait_time)
    key.tap(key.Code.TAB)
    time.sleep(wait_time)
    key.toggle(key.Code.ALT, False)
    time.sleep(wait_time)
    print("Double Alt Tabbed")


def copy_all():
    select_all()
    copy()
    print("Copied All")


def select_all():
    key.toggle(key.Code.CONTROL, True)
    time.sleep(wait_time)
    key.tap("a")
    time.sleep(wait_time)
    key.toggle(key.Code.CONTROL, False)
    time.sleep(wait_time)


def paste():
    key.toggle(key.Code.CONTROL, True)
    time.sleep(wait_time)
    key.tap("v")
    time.sleep(wait_time)
    key.toggle(key.Code.CONTROL, False)
    time.sleep(wait_time)


def copy():
    key.toggle(key.Code.CONTROL, True)
    time.sleep(wait_time)
    key.tap("c")
    time.sleep(wait_time)
    key.toggle(key.Code.CONTROL, False)
    time.sleep(wait_time)


def click_on_coordinate(coord: Coordinates):
    mouse.smooth_move(coord.x, coord.y)
    mouse.click()
    time.sleep(wait_time)

    print(f"Clicked on {coord}")


def tab():
    key.tap(key.Code.TAB)
    time.sleep(wait_time)
    print("Pressed Tab")


def enter():
    key.tap("\n")
    time.sleep(wait_time)
    print("Pressed Enter")


def copy_anki_reading():
    click_on_coordinate(MousePositions.anki_expression)
    tab()
    tab()
    copy_all()


def scroll_to_bottom():
    click_on_coordinate(MousePositions.top_scroll_bar)
    mouse.toggle(down=True)
    mouse.smooth_move(
        MousePositions.bottom_scroll_bar.x, MousePositions.bottom_scroll_bar.y
    )
    mouse.toggle(down=False)
    time.sleep(wait_time)
    print("Scrolled to bottom")


def paste_reading():
    scroll_to_bottom()
    click_on_coordinate(MousePositions.input_position)
    select_all()
    paste()
    enter()


def set_up_tab_cycle():
    alt_tab()
    alt_double_tab()
    alt_tab()


def copy_answer():
    click_on_coordinate(MousePositions.copy_position)
    time.sleep(wait_time)


def paste_answer_into_anki():
    click_on_coordinate(MousePositions.anki_expression)
    tab()
    paste()


def go_to_next_anki_card():
    click_on_coordinate(MousePositions.anki_scroll_bar)
    time.sleep(wait_time)
    key.tap(key.Code.DOWN_ARROW)


def process_one_card():
    copy_anki_reading()
    alt_tab()
    paste_reading()
    time.sleep(long_wait_time)
    copy_answer()
    alt_tab()
    paste_answer_into_anki()
    go_to_next_anki_card()


def main():
    set_up_tab_cycle()
    for i in range(30):
        process_one_card()


if __name__ == "__main__":
    main()
