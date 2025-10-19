import tkinter as tk

def sqm_to_pyeong(sqm):
    try:
        return float(sqm) / 3.3058
    except:
        return None

def pyeong_to_sqm(pyeong):
    try:
        return float(pyeong) * 3.3058
    except:
        return None

class AreaConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('면적 단위 변환기')
        self.geometry('350x220')

        self.updating = False  # 재귀 방지용

        self.font_style = ('맑은 고딕', 15)

        # 열 가중치 (중앙 정렬용)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # 변수 선언
        self.exclusive_sqm_var = tk.StringVar()
        self.supply_sqm_var = tk.StringVar()
        self.exclusive_pyeong_var = tk.StringVar()
        self.supply_pyeong_var = tk.StringVar()

        # 라벨 및 엔트리 생성
        tk.Label(self, text='[전용면적 ㎡]', font=self.font_style).grid(row=0, column=0, padx=10, pady=8, sticky='nsew')
        self.entry_exclusive_sqm = tk.Entry(self, textvariable=self.exclusive_sqm_var, bg='white', font=self.font_style, width=10, justify='right')
        self.entry_exclusive_sqm.grid(row=0, column=1, padx=30, pady=8, sticky='nsew')

        tk.Label(self, text='[공급면적 ㎡]', font=self.font_style).grid(row=1, column=0, padx=10, pady=8, sticky='nsew')
        self.entry_supply_sqm = tk.Entry(self, textvariable=self.supply_sqm_var, bg='white', font=self.font_style, width=10, justify='right')
        self.entry_supply_sqm.grid(row=1, column=1, padx=30, pady=8, sticky='nsew')

        tk.Label(self, text='[전용면적 평]', font=self.font_style).grid(row=2, column=0, padx=10, pady=8, sticky='nsew')
        self.entry_exclusive_pyeong = tk.Entry(self, textvariable=self.exclusive_pyeong_var, bg='white', font=self.font_style, width=10, justify='right')
        self.entry_exclusive_pyeong.grid(row=2, column=1, padx=30, pady=8, sticky='nsew')

        tk.Label(self, text='[공급면적 평]', font=self.font_style).grid(row=3, column=0, padx=10, pady=8, sticky='nsew')
        self.entry_supply_pyeong = tk.Entry(self, textvariable=self.supply_pyeong_var, bg='white', font=self.font_style, width=10, justify='right')
        self.entry_supply_pyeong.grid(row=3, column=1, padx=30, pady=8, sticky='nsew')

        # 이벤트 바인딩
        self.exclusive_sqm_var.trace_add('write', lambda *args: self.on_change('exclusive_sqm'))
        self.supply_sqm_var.trace_add('write', lambda *args: self.on_change('supply_sqm'))
        self.exclusive_pyeong_var.trace_add('write', lambda *args: self.on_change('exclusive_pyeong'))
        self.supply_pyeong_var.trace_add('write', lambda *args: self.on_change('supply_pyeong'))

    def on_change(self, changed):
        if self.updating:
            return
        self.updating = True

        def set_bg(entry, color):
            entry.config(bg=color)

        try:
            if changed == 'supply_sqm':
                val = self.supply_sqm_var.get()
                supply_sqm = float(val)
                exclusive_sqm = supply_sqm * 0.76
                supply_pyeong = sqm_to_pyeong(supply_sqm)
                exclusive_pyeong = sqm_to_pyeong(exclusive_sqm)

                set_bg(self.entry_supply_sqm, 'pale green')
                set_bg(self.entry_exclusive_sqm, 'light yellow')
                set_bg(self.entry_supply_pyeong, 'light yellow')
                set_bg(self.entry_exclusive_pyeong, 'light yellow')

                self.exclusive_sqm_var.set(f'{exclusive_sqm:.2f}')
                self.supply_pyeong_var.set(f'{supply_pyeong:.2f}')
                self.exclusive_pyeong_var.set(f'{exclusive_pyeong:.2f}')

            elif changed == 'exclusive_sqm':
                val = self.exclusive_sqm_var.get()
                exclusive_sqm = float(val)
                supply_sqm = exclusive_sqm / 0.76
                exclusive_pyeong = sqm_to_pyeong(exclusive_sqm)
                supply_pyeong = sqm_to_pyeong(supply_sqm)

                set_bg(self.entry_exclusive_sqm, 'pale green')
                set_bg(self.entry_supply_sqm, 'light yellow')
                set_bg(self.entry_supply_pyeong, 'light yellow')
                set_bg(self.entry_exclusive_pyeong, 'light yellow')

                self.supply_sqm_var.set(f'{supply_sqm:.2f}')
                self.exclusive_pyeong_var.set(f'{exclusive_pyeong:.2f}')
                self.supply_pyeong_var.set(f'{supply_pyeong:.2f}')

            elif changed == 'supply_pyeong':
                val = self.supply_pyeong_var.get()
                supply_pyeong = float(val)
                supply_sqm = pyeong_to_sqm(supply_pyeong)
                exclusive_sqm = supply_sqm * 0.76
                exclusive_pyeong = sqm_to_pyeong(exclusive_sqm)

                set_bg(self.entry_supply_pyeong, 'pale green')
                set_bg(self.entry_supply_sqm, 'light yellow')
                set_bg(self.entry_exclusive_sqm, 'light yellow')
                set_bg(self.entry_exclusive_pyeong, 'light yellow')

                self.supply_sqm_var.set(f'{supply_sqm:.2f}')
                self.exclusive_sqm_var.set(f'{exclusive_sqm:.2f}')
                self.exclusive_pyeong_var.set(f'{exclusive_pyeong:.2f}')

            elif changed == 'exclusive_pyeong':
                val = self.exclusive_pyeong_var.get()
                exclusive_pyeong = float(val)
                exclusive_sqm = pyeong_to_sqm(exclusive_pyeong)
                supply_sqm = exclusive_sqm / 0.76
                supply_pyeong = sqm_to_pyeong(supply_sqm)

                set_bg(self.entry_exclusive_pyeong, 'pale green')
                set_bg(self.entry_exclusive_sqm, 'light yellow')
                set_bg(self.entry_supply_sqm, 'light yellow')
                set_bg(self.entry_supply_pyeong, 'light yellow')

                self.exclusive_sqm_var.set(f'{exclusive_sqm:.2f}')
                self.supply_sqm_var.set(f'{supply_sqm:.2f}')
                self.supply_pyeong_var.set(f'{supply_pyeong:.2f}')

        except ValueError:
            set_bg(self.entry_exclusive_sqm, 'white')
            set_bg(self.entry_supply_sqm, 'white')
            set_bg(self.entry_exclusive_pyeong, 'white')
            set_bg(self.entry_supply_pyeong, 'white')

        self.updating = False

if __name__ == '__main__':
    app = AreaConverterApp()
    app.mainloop()
