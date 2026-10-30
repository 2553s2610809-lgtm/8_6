
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# 편한결제 - 노인 전용 간편 결제 앱
# 시연용 가상 결제 시스템

BG = "#EAF2FA"
BLUE = "#1769AA"
DARK_BLUE = "#174A78"
TEXT_BLUE = "#58738D"
SILVER = "#D7E0E8"
WHITE = "#FFFFFF"
FONT = "Malgun Gothic"

balance = 125000

transactions = [
    {"kind": "결제", "name": "동네 마트",
     "amount": -5000, "time": "오늘 오후 2:10"},
    {"kind": "결제", "name": "동네 약국",
     "amount": -8000, "time": "오늘 오전 11:30"},
]


def won(amount):
    return f"{amount:,}원"


class EasyPayApp:

    def __init__(self, root):
        self.root = root
        self.root.title("편한결제")
        self.root.geometry("940x590")
        self.root.minsize(760, 540)
        self.root.configure(bg=BG)
        self.show_home()

    def clear(self):
        for child in self.root.winfo_children():
            child.destroy()

    def label(self, parent, text, size=16,
              color=DARK_BLUE, bold=False, bg=WHITE):
        return tk.Label(
            parent,
            text=text,
            font=(FONT, size,
                  "bold" if bold else "normal"),
            fg=color,
            bg=bg
        )

    def button(self, parent, text, command,
               bg=WHITE, fg=DARK_BLUE,
               size=19, height=2):

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            font=(FONT, size, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            height=height
        )

    # 상단 로고 및 제목
    def header(self, parent):

        bar = tk.Frame(parent, bg=BG)
        bar.pack(fill="x", padx=14, pady=(14, 16))

        logo = tk.Label(
            bar,
            text="▣",
            bg=BLUE,
            fg=WHITE,
            font=(FONT, 26, "bold"),
            width=3,
            height=1
        )
        logo.pack(side="left", padx=(0, 12), ipady=7)

        titlebox = tk.Frame(bar, bg=BG)
        titlebox.pack(side="left")

        self.label(
            titlebox, "편한결제", 22,
            DARK_BLUE, True, BG
        ).pack(anchor="w")

        self.label(
            titlebox, "누구나 쉽고 편하게",
            13, TEXT_BLUE, False, BG
        ).pack(anchor="w")

        tk.Button(
            bar,
            text="?",
            command=self.show_help,
            bg=BG,
            fg=BLUE,
            font=(FONT, 18, "bold"),
            relief="flat",
            bd=0
        ).pack(side="right", padx=8)

    # 첫 화면
    def show_home(self):

        self.clear()
        self.root.configure(bg=BG)

        self.header(self.root)

        balance_card = tk.Frame(
            self.root, bg=WHITE
        )
        balance_card.pack(
            fill="x",
            padx=14,
            pady=(0, 14),
            ipady=17
        )

        self.label(
            balance_card, "내 잔액",
            15, TEXT_BLUE
        ).pack(anchor="w", padx=20, pady=(8, 5))

        self.label(
            balance_card, won(balance),
            28, DARK_BLUE, True
        ).pack(anchor="w", padx=20, pady=2)

        self.label(
            balance_card,
            "♢ 안전하게 관리되는 내 돈",
            14, TEXT_BLUE
        ).pack(anchor="w", padx=20, pady=(6, 4))

        grid = tk.Frame(self.root, bg=BG)
        grid.pack(
            fill="both",
            expand=True,
            padx=14,
            pady=(0, 12)
        )

        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)
        grid.rowconfigure(0, weight=1)
        grid.rowconfigure(1, weight=1)

        self.home_tile(
            grid, "▧", "결제하기",
            "QR코드로 간편하게",
            self.show_pay, BLUE, WHITE, 0, 0
        )

        self.home_tile(
            grid, "➤", "송금하기",
            "소중한 분께 간편하게",
            self.show_transfer,
            WHITE, DARK_BLUE, 0, 1
        )

        self.home_tile(
            grid, "▤", "사용 내역",
            "돈 쓴 기록 확인",
            self.show_history,
            WHITE, DARK_BLUE, 1, 0
        )

        self.home_tile(
            grid, "☏", "도움받기",
            "사용 방법 안내",
            self.show_help,
            SILVER, DARK_BLUE, 1, 1
        )

        self.label(
            self.root,
            "시연용 앱 · 실제 금융기관과 연결되어 있지 않습니다.",
            9, TEXT_BLUE, bg=BG
        ).pack(pady=(0, 7))

    # 메인 메뉴 버튼
    def home_tile(self, parent, icon, title,
                  subtitle, command, bg, fg, row, col):

        tile = tk.Frame(parent, bg=bg)

        tile.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=(0, 7) if col == 0 else (7, 0),
            pady=(0, 7) if row == 0 else (7, 0)
        )

        tile.grid_propagate(False)

        btn = tk.Button(
            tile,
            text=f"{icon}\n{title}\n{subtitle}",
            command=command,
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            font=(FONT, 17 if title == "결제하기" else 16, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            justify="center",
            wraplength=320
        )

        btn.pack(fill="both", expand=True, padx=5, pady=5)

    # 공통 화면
    def page_shell(self, title, subtitle=""):

        self.clear()
        self.root.configure(bg=BG)

        self.header(self.root)

        panel = tk.Frame(self.root, bg=WHITE)
        panel.pack(
            fill="both",
            expand=True,
            padx=14,
            pady=(0, 14)
        )

        self.label(
            panel, title, 25,
            DARK_BLUE, True
        ).pack(anchor="w", padx=24, pady=(22, 4))

        if subtitle:
            self.label(
                panel, subtitle, 14,
                TEXT_BLUE
            ).pack(anchor="w", padx=24, pady=(0, 16))

        return panel

    # 입력창
    def make_entry(self, parent, caption, initial=""):

        self.label(
            parent, caption, 16,
            DARK_BLUE, True
        ).pack(anchor="w", padx=24, pady=(12, 5))

        entry = tk.Entry(
            parent,
            font=(FONT, 19),
            relief="solid",
            bd=1,
            fg=DARK_BLUE
        )

        entry.pack(fill="x", padx=24, ipady=9)

        if initial:
            entry.insert(0, initial)

        return entry

    # 하단 버튼
    def make_action_row(self, parent,
                        primary_text, primary_command):

        row = tk.Frame(parent, bg=WHITE)
        row.pack(fill="x", padx=24, pady=20)

        self.button(
            row, "처음으로",
            self.show_home,
            SILVER, DARK_BLUE,
            14, 1
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 8),
            ipady=5
        )

        self.button(
            row, primary_text,
            primary_command,
            BLUE, WHITE,
            14, 1
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(8, 0),
            ipady=5
        )

    # 결제 화면
    def show_pay(self):

        panel = self.page_shell(
            "결제하기",
            "결제할 곳과 금액을 입력해 주세요."
        )

        shop = self.make_entry(
            panel, "가게 이름", "동네 가게"
        )

        amount = self.make_entry(
            panel, "결제 금액 (원)"
        )

        self.label(
            panel,
            f"현재 잔액: {won(balance)}",
            15, TEXT_BLUE
        ).pack(anchor="w", padx=24, pady=12)

        def confirm():

            name = shop.get().strip() or "가게"
            value = self.parse_amount(amount.get())

            if value is None:
                return

            if value > balance:
                messagebox.showwarning(
                    "잔액 부족",
                    "잔액이 부족합니다. 금액을 확인해 주세요."
                )
                return

            if not messagebox.askyesno(
                "결제 확인",
                f"{name}에서 {won(value)} 결제할까요?"
            ):
                return

            self.add_transaction(
                "결제", name, -value
            )

            messagebox.showinfo(
                "결제 완료",
                f"{won(value)} 결제가 완료되었습니다.\n(시연용)"
            )

            self.show_home()

        self.make_action_row(
            panel, "결제 확인", confirm
        )

    # 송금 화면
    def show_transfer(self):

        panel = self.page_shell(
            "송금하기",
            "받는 분과 금액을 확인한 뒤 송금해 주세요."
        )

        recipient = self.make_entry(
            panel, "받는 분 이름"
        )

        amount = self.make_entry(
            panel, "송금 금액 (원)"
        )

        self.label(
            panel,
            f"현재 잔액: {won(balance)}",
            15, TEXT_BLUE
        ).pack(anchor="w", padx=24, pady=12)

        def confirm():

            name = recipient.get().strip()

            if not name:
                messagebox.showwarning(
                    "이름 확인",
                    "받는 분 이름을 입력해 주세요."
                )
                return

            value = self.parse_amount(amount.get())

            if value is None:
                return

            if value > balance:
                messagebox.showwarning(
                    "잔액 부족",
                    "잔액이 부족합니다."
                )
                return

            if not messagebox.askyesno(
                "송금 확인",
                f"{name}님에게 {won(value)} 송금할까요?\n\n시연용 가상 송금입니다."
            ):
                return

            self.add_transaction(
                "송금", name, -value
            )

            messagebox.showinfo(
                "송금 완료",
                f"{name}님에게 {won(value)} 송금 처리되었습니다.\n(시연용)"
            )

            self.show_home()

        self.make_action_row(
            panel, "송금 확인", confirm
        )

    # 금액 확인
    def parse_amount(self, raw):

        try:
            value = int(raw.replace(",", "").strip())

            if value <= 0:
                raise ValueError

            return value

        except (ValueError, AttributeError):

            messagebox.showwarning(
                "금액 확인",
                "0보다 큰 금액을 숫자로 입력해 주세요."
            )

            return None

    # 거래 기록 및 잔액 변경
    def add_transaction(self, kind, name, amount):

        global balance

        balance += amount

        transactions.insert(0, {
            "kind": kind,
            "name": name,
            "amount": amount,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    # 사용 내역 화면
    def show_history(self):

        panel = self.page_shell(
            "사용 내역",
            "최근 결제 및 송금 기록입니다."
        )

        if not transactions:

            self.label(
                panel, "아직 사용 내역이 없습니다.",
                17, TEXT_BLUE
            ).pack(anchor="w", padx=24, pady=20)

        else:

            for item in transactions:

                row = tk.Frame(
                    panel,
                    bg=WHITE,
                    highlightbackground="#DCE5ED",
                    highlightthickness=1
                )

                row.pack(fill="x", padx=24, pady=5)

                left = tk.Frame(row, bg=WHITE)
                left.pack(
                    side="left",
                    fill="x",
                    expand=True,
                    padx=12,
                    pady=9
                )

                self.label(
                    left,
                    f"{item['kind']} · {item['name']}",
                    15, DARK_BLUE, True
                ).pack(anchor="w")

                self.label(
                    left, item["time"],
                    11, TEXT_BLUE
                ).pack(anchor="w", pady=(3, 0))

                color = (
                    BLUE if item["amount"] > 0
                    else DARK_BLUE
                )

                self.label(
                    row,
                    f"{item['amount']:+,}원",
                    15, color, True
                ).pack(side="right", padx=14)

        self.button(
            panel, "홈으로 돌아가기",
            self.show_home,
            BLUE, WHITE, 15, 1
        ).pack(fill="x", padx=24, pady=20, ipady=5)

    # 도움말 화면
    def show_help(self):

        panel = self.page_shell(
            "도움받기",
            "편한결제를 사용하는 방법을 안내해 드립니다."
        )

        tips = [
            (
                "1. 결제하기",
                "가게 이름과 금액을 입력하고 결제 확인을 누르세요."
            ),
            (
                "2. 송금하기",
                "받는 분 이름과 금액을 입력한 뒤 내용을 확인하세요."
            ),
            (
                "3. 사용 내역",
                "결제와 송금 기록을 확인할 수 있습니다."
            ),
            (
                "4. 안전하게 사용하기",
                "확인 화면에서 이름과 금액을 꼭 살펴보세요."
            )
        ]

        for heading, desc in tips:

            block = tk.Frame(panel, bg=WHITE)
            block.pack(fill="x", padx=24, pady=8)

            self.label(
                block, heading,
                16, DARK_BLUE, True
            ).pack(anchor="w")

            self.label(
                block, desc,
                13, TEXT_BLUE
            ).pack(anchor="w", pady=(3, 0))

        self.button(
            panel, "홈으로 돌아가기",
            self.show_home,
            BLUE, WHITE, 15, 1
        ).pack(fill="x", padx=24, pady=18, ipady=5)


# 프로그램 실행
if __name__ == "__main__":

    root = tk.Tk()

    app = EasyPayApp(root)

    root.mainloop()

