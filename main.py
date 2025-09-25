import sys
from scrapper_stolnik import all_prices
import write_to_gsheet


def main():
    print("🚀 Старт парсинга и загрузки цен в Google Sheets")

    try:
        print(f"✅ Собрано {len(all_prices)} цен с сайта")
        print("📤 Загружаем данные в Google Sheets...")
        print("✅ Данные успешно загружены")

    except Exception as e:
        print(f"❌ Ошибка выполнения: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()