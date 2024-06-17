import flet as ft


class Field:
    name: str
    type: str


class Sheet:
    name: str
    list_of_fields: list[str]


class Workbook:
    name: str
    list_of_sheets: list[Sheet]


class Csv:
    sheet: Sheet


class Json:
    sheet: Sheet


class Parquet:
    sheet: Sheet


class File:
    path: str
    name: str

    file_type: str
    file: Workbook | Csv | Json | Parquet


class Task:
    name: str


class Workflow:
    name: str
    list_of_files: list[File]
    target: dict[str, str]  # File (parquet/csv/etc) / Database connection
    job: Task


def main(page: ft.Page):
    page.title = "Yoinker App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        for file in selected_files.value.split(", "):
            unselected.options.append(ft.dropdown.Option(file))
        page.update()

    def find_option(option_name):
        for option in unselected.options:
            if option_name == option.key:
                return option
        return None

    def add_selected(e):
        option = find_option(unselected.value)
        if option != None:
            selected.options.append(option)
            unselected.options.remove(option)
            page.update()
        page.update()

    def remove_selected(e):
        option = find_option(selected.value)
        if option != None:
            unselected.options.append(option)
            selected.options.remove(option)
            page.update()
        page.update()

    def file_selected(e):
        f.value = f"File selected: {unselected.value}"
        page.update()

    def workbook_selected(e):
        w.value = f"Workbook selected: {selected.value}"
        page.update()

    def tab_selected(e):
        t.value = f"Tab selected: {selected.value}"
        page.update()

    def workbooks_changed(e):

        workbooks_left = ft.Text("0 tabs selected")
        status = filter.tabs[filter.selected_index].text
        count = 0

        for tab in workbook_selected.controls:
            tab.visible = status == "all" or (status == "selected") or (status == "unselected")
            if not tab.completed:
                count += 1

        workbooks_left.value = f"{count} active tabs(s) selected"

    def fields_changed(e):

        fields_changed = ft.Text("0 fields selected")
        status = filter.fields[filter.selected_index].text
        count = 0

        for field in tab_selected.controls:
            field.visible = status == "all" or (status == "selected") or (status == "unselected")
            if not field.completed:
                count += 1
        fields_changed.value = f"{count} active fields(s) selected"

    file_picker = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(file_picker)

    workbookTabs = ft.Column(
        [
            ft.Divider(),
            ft.Text("Workbooks"),
            ft.Container(
                width=410,
                bgcolor=ft.colors.GREEN,
            ),
            ft.Tabs(
                scrollable=False,
                selected_index=0,
                on_change=workbooks_changed,
                tabs=[
                    ft.Tab(text="all"),
                    ft.Tab(text="selected"),
                    ft.Tab(text="unselected"),
                ],
            ),
        ],
        width=400,
    )

    fieldTabs = ft.Column(
        [
            ft.Divider(),
            ft.Text("Fields"),
            ft.Container(
                width=410,
                bgcolor=ft.colors.BLUE,
            ),
            ft.Tabs(
                scrollable=False,
                selected_index=0,
                on_change=fields_changed,
                tabs=[
                    ft.Tab(text="all"),
                    ft.Tab(text="selected"),
                    ft.Tab(text="unselected"),
                ],
            ),
        ],
        width=400,
    )
    f = ft.Text()
    w = ft.Text()
    # application's root control (i.e. "view") containing all other controls
    col = ft.Column(
        [  # File Picker Button
            ft.ElevatedButton(
                "Pick files",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: file_picker.pick_files(
                    # Allow multiple files to be selected and limit the file types
                    allow_multiple=True,
                    allowed_extensions=["xlsx", "xls", "csv", "json", "parquet", "txt"],
                ),
            ),
            # self.selected_files,
        ],
    )

    selected = ft.Dropdown(
        label="File",
        on_change=workbook_selected,
        hint_text="Selected files",
        options=[],
        width=400,
    )

    unselected = ft.Dropdown(
        label="File",
        on_change=file_selected,
        hint_text="Unselected files",
        options=[],
        width=400,
    )

    add = ft.ElevatedButton("Add", on_click=add_selected)
    remove = ft.ElevatedButton("Remove", on_click=remove_selected)

    # create app control and add it to the page
    page.add(col)
    page.add(unselected, add, f)
    page.add(selected, remove, w)
    page.add(workbookTabs)
    page.add(fieldTabs)


ft.app(main)
