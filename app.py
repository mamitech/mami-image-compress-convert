#!/usr/bin/env python3

import os
import sys
import argparse
from PIL import Image, ImageOps
import glob
from pathlib import Path
import time
from typing import Optional, Tuple, Union, List
import psutil

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ImageCompressor:
    def __init__(self):
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        self.input_dir = Path('./input')
        self.output_dir = Path('./output')
        # Memory management constants
        self.MAX_IMAGE_SIZE_MB = 100  # Maximum image size in MB
        self.MAX_PIXELS = 50_000_000   # Maximum pixels (e.g., ~7000x7000)

    def print_header(self):
        print(f"\n{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗{Colors.ENDC}")
        print(f"{Colors.CYAN}{Colors.BOLD}║                    🖼️  IMAGE COMPRESSOR  🖼️                 ║{Colors.ENDC}")
        print(f"{Colors.CYAN}{Colors.BOLD}╚════════════════════════════════════════════════════════════╝{Colors.ENDC}\n")

    def get_output_format(self):
        print(f"\n{Colors.BLUE}{Colors.BOLD}📝 Output Format Selection{Colors.ENDC}\n")

        print("Select output format:")
        print(f"  {Colors.GREEN}1.{Colors.ENDC} Keep Original  (same as input format) {Colors.BOLD}[RECOMMENDED]{Colors.ENDC}")
        print(f"  {Colors.YELLOW}2.{Colors.ENDC} JPEG (.jpg)    (best compression, no transparency)")
        print(f"  {Colors.CYAN}3.{Colors.ENDC} PNG (.png)     (lossless, supports transparency)")
        print(f"  {Colors.BLUE}4.{Colors.ENDC} WebP (.webp)   (modern format, excellent compression)")

        while True:
            choice = input(f"\n{Colors.BOLD}Enter your choice (1-4, or press Enter for recommended):{Colors.ENDC} ").strip()
            if choice == '' or choice == '1':
                return None, "Original Format"
            elif choice == '2':
                return '.jpg', "JPEG"
            elif choice == '3':
                return '.png', "PNG"
            elif choice == '4':
                return '.webp', "WebP"
            else:
                print(f"{Colors.RED}Invalid choice. Please select 1, 2, 3, 4, or press Enter for recommended.{Colors.ENDC}")

    def get_processing_mode(self):
        print(f"\n{Colors.BLUE}{Colors.BOLD}⚙️  Processing Mode Selection{Colors.ENDC}\n")

        print("Choose processing mode:")
        print(f"  {Colors.GREEN}1.{Colors.ENDC} Compress + Convert (compress quality, then convert format)")
        print(f"  {Colors.YELLOW}2.{Colors.ENDC} Convert + Compress (convert format first, then compress quality)")
        print(f"  {Colors.CYAN}3.{Colors.ENDC} Compress Only      (reduce quality, keep original format)")
        print(f"  {Colors.BLUE}4.{Colors.ENDC} Convert Only       (change format, keep original quality) {Colors.BOLD}[RECOMMENDED]{Colors.ENDC}")

        while True:
            choice = input(f"\n{Colors.BOLD}Enter your choice (1-4, or press Enter for recommended):{Colors.ENDC} ").strip()
            if choice == '' or choice == '4':
                return "convert_only", "Convert Only"
            elif choice == '1':
                return "compress_convert", "Compress + Convert"
            elif choice == '2':
                return "convert_compress", "Convert + Compress"
            elif choice == '3':
                return "compress_only", "Compress Only"
            else:
                print(f"{Colors.RED}Invalid choice. Please select 1, 2, 3, 4, or press Enter for recommended.{Colors.ENDC}")

    def get_output_suffix(self, default_suffix: str):
        print(f"\n{Colors.BLUE}{Colors.BOLD}📝 Output Filename Settings{Colors.ENDC}\n")

        print("Choose output filename format:")
        print(f"  {Colors.GREEN}1.{Colors.ENDC} Add suffix to filename {Colors.BOLD}[RECOMMENDED]{Colors.ENDC}")
        print(f"  {Colors.YELLOW}2.{Colors.ENDC} Keep original filename (no suffix)")

        while True:
            choice = input(f"\n{Colors.BOLD}Enter your choice (1-2, or press Enter for recommended):{Colors.ENDC} ").strip()
            if choice == '' or choice == '1':
                # Prompt for custom suffix (default depends on mode)
                print(f"\n{Colors.CYAN}Enter suffix for output files:{Colors.ENDC}")
                print(f"Example: '{default_suffix}' will rename 'photo.jpg' to 'photo{default_suffix}.jpg'")
                suffix = input(f"{Colors.BOLD}Suffix (press Enter for '{default_suffix}'):{Colors.ENDC} ").strip()
                if not suffix:
                    suffix = default_suffix
                elif not suffix.startswith('-') and not suffix.startswith('_'):
                    # Add separator if user omitted it
                    suffix = f"-{suffix}"
                return suffix
            elif choice == '2':
                return ""  # Empty suffix means keep original name
            else:
                print(f"{Colors.RED}Invalid choice. Please select 1, 2, or press Enter for recommended.{Colors.ENDC}")

    def get_compression_settings(self):
        print(f"{Colors.BLUE}{Colors.BOLD}📋 Compression Configuration{Colors.ENDC}\n")

        # Processing mode selection
        mode, mode_name = self.get_processing_mode()

        quality, quality_name = None, None
        output_ext, format_name = None, None

        # Get compression settings if needed
        if mode in ["compress_convert", "convert_compress", "compress_only"]:
            print(f"\n{Colors.BLUE}{Colors.BOLD}🎯 Quality Settings{Colors.ENDC}\n")
            print("Select compression quality:")
            print(f"  {Colors.GREEN}1.{Colors.ENDC} High Quality   (90% quality, ~30% size reduction)")
            print(f"  {Colors.YELLOW}2.{Colors.ENDC} Medium Quality (80% quality, ~45% size reduction) {Colors.BOLD}[RECOMMENDED]{Colors.ENDC}")
            print(f"  {Colors.RED}3.{Colors.ENDC} Low Quality    (60% quality, ~65% size reduction)")
            print(f"  {Colors.CYAN}4.{Colors.ENDC} Custom Quality (specify your own percentage)")

            while True:
                choice = input(f"\n{Colors.BOLD}Enter your choice (1-4, or press Enter for recommended):{Colors.ENDC} ").strip()
                if choice == '' or choice == '2':
                    quality, quality_name = 80, "Medium (Recommended)"
                    break
                elif choice == '1':
                    quality, quality_name = 90, "High"
                    break
                elif choice == '3':
                    quality, quality_name = 60, "Low"
                    break
                elif choice == '4':
                    while True:
                        try:
                            custom_quality = int(input(f"Enter quality percentage (1-100): "))
                            if 1 <= custom_quality <= 100:
                                quality, quality_name = custom_quality, "Custom"
                                break
                            print(f"{Colors.RED}Please enter a value between 1 and 100.{Colors.ENDC}")
                        except ValueError:
                            print(f"{Colors.RED}Please enter a valid number.{Colors.ENDC}")
                    break
                else:
                    print(f"{Colors.RED}Invalid choice. Please select 1, 2, 3, 4, or press Enter for recommended.{Colors.ENDC}")

        # Get format settings if needed
        if mode in ["compress_convert", "convert_compress", "convert_only"]:
            output_ext, format_name = self.get_output_format()

        # Determine default suffix based on processing mode
        if mode == "convert_only":
            default_suffix_val = "-converted"
        else:
            default_suffix_val = "-compressed"
        # Get suffix settings (default varies by mode)
        suffix = self.get_output_suffix(default_suffix_val)

        return quality, quality_name, output_ext, format_name, mode, mode_name, suffix

    def _validate_image_file(self, file_path: str) -> bool:
        """Validate image file for safety and size constraints"""
        try:
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

            # Check file size limit
            if file_size_mb > self.MAX_IMAGE_SIZE_MB:
                print(f"{Colors.YELLOW}⚠️  Warning: {Path(file_path).name} ({file_size_mb:.1f}MB) exceeds size limit ({self.MAX_IMAGE_SIZE_MB}MB), skipping{Colors.ENDC}")
                return False

            # Try to open and validate the image
            with Image.open(file_path) as img:
                # Check image dimensions
                width, height = img.size
                total_pixels = width * height

                if total_pixels > self.MAX_PIXELS:
                    print(f"{Colors.YELLOW}⚠️  Warning: {Path(file_path).name} ({width}×{height}) exceeds pixel limit, skipping{Colors.ENDC}")
                    return False

                # Verify image integrity by loading a small portion
                img.verify()

            return True

        except Exception as e:
            print(f"{Colors.RED}❌ Invalid image file {Path(file_path).name}: {str(e)}{Colors.ENDC}")
            return False

    def scan_input_folder(self) -> List[str]:
        if not self.input_dir.exists():
            print(f"{Colors.RED}❌ Input folder not found!{Colors.ENDC}")
            print(f"Please create the 'input' folder and add your images.")
            return []

        image_files = []
        for ext in self.supported_formats:
            pattern = str(self.input_dir / f"*{ext}")
            image_files.extend(glob.glob(pattern, recursive=False))
            pattern = str(self.input_dir / f"*{ext.upper()}")
            image_files.extend(glob.glob(pattern, recursive=False))

        # Validate all found files
        validated_files = []
        for file_path in sorted(list(set(image_files))):
            if self._validate_image_file(file_path):
                validated_files.append(file_path)

        return validated_files

    def display_found_images(self, image_files):
        if not image_files:
            print(f"{Colors.RED}❌ No supported image files found in the input folder!{Colors.ENDC}")
            print(f"Supported formats: {', '.join(self.supported_formats)}")
            return False

        print(f"{Colors.GREEN}{Colors.BOLD}📁 Found {len(image_files)} image(s) in input folder:{Colors.ENDC}\n")

        for i, file_path in enumerate(image_files, 1):
            file_name = Path(file_path).name
            try:
                with Image.open(file_path) as img:
                    size = img.size
                    file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB
                print(f"  {Colors.CYAN}{i:2d}.{Colors.ENDC} {file_name}")
                print(f"      📐 {size[0]}x{size[1]} pixels | 💾 {file_size:.2f} MB")
            except Exception as e:
                print(f"  {Colors.RED}{i:2d}.{Colors.ENDC} {file_name} (Error: {str(e)})")

        return True

    def confirm_processing(self):
        print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  Are these the correct images to compress?{Colors.ENDC}")
        while True:
            response = input(f"Continue with compression? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            print(f"{Colors.RED}Please enter 'y' or 'n'.{Colors.ENDC}")

    def get_output_filename(self, input_path, output_ext=None, suffix="-compressed"):
        input_file = Path(input_path)
        name_without_ext = input_file.stem
        extension = output_ext if output_ext else input_file.suffix

        # Handle no suffix mode (keep original name)
        if suffix == "":
            # Keep original filename, save to output directory
            output_name = f"{name_without_ext}{extension}"
            output_path = self.output_dir / output_name

            # Check if file already exists in output directory
            if output_path.exists():
                print(f"\n{Colors.YELLOW}⚠️  File '{output_name}' already exists in output directory.{Colors.ENDC}")
                while True:
                    choice = input("Choose: (r)eplace, (s)kip, or (n)ew name? ").strip().lower()
                    if choice in ['r', 'replace']:
                        return output_path
                    elif choice in ['s', 'skip']:
                        return None
                    elif choice in ['n', 'new', 'new name']:
                        # Add numbered suffix for conflict resolution
                        counter = 2
                        while True:
                            output_name = f"{name_without_ext}-{counter}{extension}"
                            output_path = self.output_dir / output_name
                            if not output_path.exists():
                                return output_path
                            counter += 1
                    print(f"{Colors.RED}Please enter 'r', 's', or 'n'.{Colors.ENDC}")

            return output_path

        # Normal suffix mode
        counter = 0
        while True:
            if counter == 0:
                output_name = f"{name_without_ext}{suffix}{extension}"
            else:
                output_name = f"{name_without_ext}{suffix}-{counter + 1}{extension}"

            output_path = self.output_dir / output_name

            if not output_path.exists():
                return output_path

            # File exists, ask user
            print(f"\n{Colors.YELLOW}⚠️  File '{output_name}' already exists.{Colors.ENDC}")
            while True:
                choice = input("Choose: (r)eplace, (s)kip, or (n)ew name? ").strip().lower()
                if choice in ['r', 'replace']:
                    return output_path
                elif choice in ['s', 'skip']:
                    return None
                elif choice in ['n', 'new', 'new name']:
                    counter += 1
                    break
                print(f"{Colors.RED}Please enter 'r', 's', or 'n'.{Colors.ENDC}")

    def compress_image(self, input_path, output_path, quality, mode="compress_convert"):
        try:
            with Image.open(input_path) as img:
                # Apply EXIF orientation first
                img = ImageOps.exif_transpose(img)

                # Determine target format from output path extension
                output_ext = output_path.suffix.lower()
                input_ext = Path(input_path).suffix.lower()

                # Handle different processing modes
                if mode == "convert_only":
                    # Convert format only, keep original quality
                    img = self._convert_format_only(img, output_ext)
                elif mode == "compress_only":
                    # Compress only, keep original format
                    output_ext = input_ext  # Use original format
                    img = self._compress_quality_only(img, output_ext, quality)
                elif mode == "convert_compress":
                    # Convert format first, then compress
                    img = self._convert_format_only(img, output_ext)
                    img = self._compress_quality_only(img, output_ext, quality)
                else:  # "compress_convert" (default)
                    # Compress quality first, then convert format
                    temp_img = self._compress_quality_only(img, input_ext, quality)
                    img = self._convert_format_only(temp_img, output_ext)

                # Final save with proper format handling
                self._save_image(img, output_path, output_ext, quality)
                return True
        except Exception as e:
            print(f"{Colors.RED}❌ Error compressing {Path(input_path).name}: {str(e)}{Colors.ENDC}")
            return False

    def _convert_format_only(self, img, target_ext):
        """Convert image format without quality loss"""
        if target_ext in ['.jpg', '.jpeg']:
            # JPEG doesn't support transparency, add white background
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])
                else:  # LA mode
                    background.paste(img.convert('RGB'), mask=img.split()[-1])
                return background
            elif img.mode == 'P':
                return img.convert('RGB')
        elif target_ext == '.png':
            # PNG supports all modes
            if img.mode == 'P' and 'transparency' in img.info:
                return img.convert('RGBA')
        elif target_ext == '.webp':
            # WebP supports transparency
            if img.mode not in ('RGB', 'RGBA', 'L'):
                if img.mode == 'P':
                    return img.convert('RGBA' if 'transparency' in img.info else 'RGB')
                return img.convert('RGB')
        elif target_ext == '.bmp':
            # BMP doesn't support transparency well
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])
                else:
                    background.paste(img.convert('RGB'), mask=img.split()[-1])
                return background
            elif img.mode == 'P':
                return img.convert('RGB')

        return img  # No conversion needed

    def _compress_quality_only(self, img: Image.Image, format_ext: str, quality: int) -> Image.Image:
        """Apply quality-based processing without changing format"""
        # For lossy formats, we can apply some preprocessing
        if format_ext.lower() in ['.jpg', '.jpeg', '.webp']:
            # For JPEG/WebP, ensure appropriate color mode
            if img.mode not in ('RGB', 'L'):
                if img.mode in ('RGBA', 'LA'):
                    # Add white background for transparency
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[-1])
                    else:
                        background.paste(img.convert('RGB'), mask=img.split()[-1])
                    return background
                else:
                    img = img.convert('RGB')

        # For PNG, optimize palette if applicable
        elif format_ext.lower() == '.png':
            if img.mode == 'P' and len(img.getcolors() or []) > 256:
                # Convert to RGBA if too many colors for palette
                img = img.convert('RGBA' if 'transparency' in img.info else 'RGB')

        return img

    def _save_image(self, img, output_path, output_ext, quality):
        """Save image with appropriate format settings"""
        if output_ext in ['.jpg', '.jpeg']:
            img.save(output_path, 'JPEG', quality=quality or 95, optimize=True, progressive=True)
        elif output_ext == '.png':
            if img.mode == 'P' and len(img.getcolors() or []) <= 256:
                img.save(output_path, 'PNG', optimize=True)
            else:
                img.save(output_path, 'PNG', optimize=True, compress_level=6)
        elif output_ext == '.webp':
            img.save(output_path, 'WebP', quality=quality or 95, optimize=True, lossless=False)
        elif output_ext == '.bmp':
            img.save(output_path, 'BMP')
        elif output_ext in ['.tiff', '.tif']:
            img.save(output_path, 'TIFF', quality=quality or 95, optimize=True)
        else:
            # Fallback
            img.save(output_path, optimize=True)

    def print_progress_bar(self, current, total, width=50):
        progress = current / total
        filled_width = int(width * progress)
        bar = '█' * filled_width + '░' * (width - filled_width)
        percentage = progress * 100
        print(f"\r{Colors.GREEN}[{bar}] {percentage:5.1f}% ({current}/{total}){Colors.ENDC}", end='', flush=True)

    def process_images(self, image_files, quality, quality_name, output_ext=None, format_name="Original Format", mode="compress_convert", mode_name="Compress + Convert", suffix="-compressed"):
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)

        # Create appropriate status message based on mode
        if mode == "compress_only":
            status_msg = f"🔄 Processing images: {mode_name} ({quality_name} - {quality}%)"
        elif mode == "convert_only":
            status_msg = f"🔄 Processing images: {mode_name} → {format_name}"
        else:
            status_msg = f"🔄 Processing images: {mode_name} ({quality_name} - {quality}%) → {format_name}"

        print(f"\n{Colors.BLUE}{Colors.BOLD}{status_msg}{Colors.ENDC}\n")

        successful = 0
        skipped = 0
        failed = 0

        for i, input_path in enumerate(image_files):
            file_name = Path(input_path).name

            # Show progress
            self.print_progress_bar(i, len(image_files))
            print(f"\n{Colors.CYAN}📸 Processing: {file_name}{Colors.ENDC}")

            # Get output filename
            output_path = self.get_output_filename(input_path, output_ext, suffix)
            if output_path is None:
                print(f"{Colors.YELLOW}⏭️  Skipped: {file_name}{Colors.ENDC}")
                skipped += 1
                continue

            # Get file sizes
            original_size = os.path.getsize(input_path) / (1024 * 1024)

            # Process image with selected mode
            if self.compress_image(input_path, output_path, quality, mode):
                compressed_size = os.path.getsize(output_path) / (1024 * 1024)
                reduction = ((original_size - compressed_size) / original_size) * 100

                print(f"   {Colors.GREEN}✅ Success:{Colors.ENDC} {original_size:.2f}MB → {compressed_size:.2f}MB ({reduction:.1f}% reduction)")
                print(f"   {Colors.BLUE}💾 Saved as:{Colors.ENDC} {output_path.name}")
                successful += 1
            else:
                failed += 1

            # Small delay for visual effect
            time.sleep(0.1)

        # Final progress bar
        self.print_progress_bar(len(image_files), len(image_files))

        # Print summary
        print(f"\n\n{Colors.GREEN}{Colors.BOLD}📊 Compression Summary:{Colors.ENDC}")
        print(f"   ✅ Successfully compressed: {Colors.GREEN}{successful}{Colors.ENDC}")
        if skipped > 0:
            print(f"   ⏭️  Skipped: {Colors.YELLOW}{skipped}{Colors.ENDC}")
        if failed > 0:
            print(f"   ❌ Failed: {Colors.RED}{failed}{Colors.ENDC}")

        if successful > 0:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Compression completed! Check the output folder for your compressed images.{Colors.ENDC}")

def main():
    try:
        # Change to the project directory
        script_dir = Path(__file__).parent
        os.chdir(script_dir)

        compressor = ImageCompressor()
        compressor.print_header()

        # Scan for images
        image_files = compressor.scan_input_folder()
        if not compressor.display_found_images(image_files):
            sys.exit(1)

        # Confirm with user
        if not compressor.confirm_processing():
            print(f"\n{Colors.YELLOW}Operation cancelled by user.{Colors.ENDC}")
            sys.exit(0)

        # Get compression settings
        quality, quality_name, output_ext, format_name, mode, mode_name, suffix = compressor.get_compression_settings()

        # Process images
        compressor.process_images(image_files, quality, quality_name, output_ext, format_name, mode, mode_name, suffix)

    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Operation cancelled by user.{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {str(e)}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
