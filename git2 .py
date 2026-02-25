import os
import shutil
from pathlib import Path

class FileOrganizer:
    """
    یک کلاس تمیز و زیبا برای مرتب‌سازی خودکار فایل‌ها
    """
    
    # دسته‌بندی فایل‌ها بر اساس پسوند
    FILE_CATEGORIES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
        'Audios': ['.mp3', '.wav', '.aac', '.ogg', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Programs': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.php'],
        'Executables': ['.exe', '.msi', '.app', '.deb', '.rpm'],
    }

    def __init__(self, directory_path):
        """
        مقداردهی اولیه با مسیر پوشه مورد نظر
        """
        self.directory = Path(directory_path)
        self.organized_count = 0
        self.errors = []

    def create_category_folders(self):
        """
        ساخت پوشه‌های مورد نیاز برای دسته‌بندی فایل‌ها
        """
        for category in self.FILE_CATEGORIES.keys():
            folder_path = self.directory / category
            folder_path.mkdir(exist_ok=True)
            print(f"📁 پوشه {category} ایجاد شد.")

    def get_file_category(self, file_extension):
        """
        تشخیص دسته‌بندی فایل بر اساس پسوند
        """
        file_extension = file_extension.lower()
        for category, extensions in self.FILE_CATEGORIES.items():
            if file_extension in extensions:
                return category
        return 'Others'  # فایل‌های بدون دسته‌بندی

    def organize_files(self):
        """
        مرتب‌سازی فایل‌ها در پوشه‌های مربوطه
        """
        # ساخت پوشه Others برای فایل‌های متفرقه
        (self.directory / 'Others').mkdir(exist_ok=True)
        
        # ایجاد پوشه‌های دسته‌بندی
        self.create_category_folders()

        # پیمایش تمام فایل‌ها در پوشه
        for item in self.directory.iterdir():
            if item.is_file():
                self._move_file(item)

        # نمایش گزارش نهایی
        self._show_report()

    def _move_file(self, file_path):
        """
        انتقال فایل به پوشه مناسب (متد خصوصی)
        """
        try:
            # دریافت پسوند فایل
            file_extension = file_path.suffix
            
            # اگر فایل بدون پسوند است
            if not file_extension:
                destination = self.directory / 'Others'
            else:
                category = self.get_file_category(file_extension)
                destination = self.directory / category

            # اگر فایل در پوشه مقصد وجود دارد، نام آن را تغییر می‌دهیم
            destination_path = destination / file_path.name
            if destination_path.exists():
                new_name = self._get_unique_filename(destination, file_path.stem, file_extension)
                destination_path = destination / new_name

            # انتقال فایل
            shutil.move(str(file_path), str(destination_path))
            self.organized_count += 1
            print(f"✅ {file_path.name} -> {destination.name}")

        except Exception as e:
            self.errors.append(f"خطا در انتقال {file_path.name}: {str(e)}")

    def _get_unique_filename(self, destination, stem, extension):
        """
        ایجاد نام یکتا برای فایل‌های تکراری
        """
        counter = 1
        while True:
            new_name = f"{stem}_{counter}{extension}"
            if not (destination / new_name).exists():
                return new_name
            counter += 1

    def _show_report(self):
        """
        نمایش گزارش نهایی مرتب‌سازی
        """
        print("\n" + "="*50)
        print("📊 گزارش نهایی مرتب‌سازی:")
        print("="*50)
        print(f"✅ تعداد فایل‌های مرتب شده: {self.organized_count}")
        
        if self.errors:
            print(f"❌ تعداد خطاها: {len(self.errors)}")
            for error in self.errors:
                print(f"   • {error}")
        else:
            print("✨ بدون خطا!")
        
        print("="*50)


def main():
    """
    تابع اصلی برای اجرای برنامه
    """
    print("🚀 برنامه مرتب‌ساز فایل‌ها")
    print("-" * 30)
    
    # دریافت مسیر از کاربر
    while True:
        directory = input("📂 مسیر پوشه مورد نظر را وارد کنید: ").strip()
        
        # حذف نقل قول‌های اضافی اگر کاربر مسیر را با نقل قول کپی کرده باشد
        directory = directory.strip('"').strip("'")
        
        if os.path.exists(directory):
            break
        else:
            print("❌ مسیر وارد شده وجود ندارد! لطفاً دوباره تلاش کنید.")
    
    # ایجاد شیء مرتب‌ساز و اجرا
    organizer = FileOrganizer(directory)
    
    print("\n🔄 در حال مرتب‌سازی فایل‌ها...\n")
    organizer.organize_files()
    
    print("\n🎉 مرتب‌سازی با موفقیت انجام شد!")


if __name__ == "__main__":
    main()

         
    