# 🖼️ Mami Image Compressor & Converter

A powerful, user-friendly terminal application for image compression and format conversion with an intuitive step-by-step interface.

## ✨ Key Features

### 🎯 **Processing Modes**
- **Convert Only** *(recommended)*: Change format while preserving quality
- **Compress Only**: Reduce file size while keeping original format
- **Compress + Convert**: Reduce quality first, then convert format
- **Convert + Compress**: Convert format first, then reduce quality

### 🖼️ **Format Support**
- **Input formats**: JPEG, PNG, BMP, TIFF, WebP
- **Output formats**: JPEG, PNG, WebP, BMP, TIFF
- **Smart conversion**: Handles transparency, color modes, and format-specific optimizations

### 📊 **Quality Options**
- **High Quality** (90%): ~30% size reduction
- **Medium Quality** (80%): ~45% size reduction *(recommended)*
- **Low Quality** (60%): ~65% size reduction
- **Custom Quality**: Specify any percentage (1-100%)

### 📝 **Filename Control**
- **Add suffix**: Customize output naming (default: "-compressed" or "-converted" for Convert Only mode)
- **Keep original**: Maintain same filename in output folder
- **Smart conflict resolution**: Auto-numbering for duplicates

### ✨ **User Experience**
- **Beautiful terminal UI**: Colors, progress bars, and clear feedback
- **Batch processing**: Handle multiple images simultaneously
- **Safe workflow**: Input and output folders keep originals protected
- **Interactive guidance**: Step-by-step configuration with smart defaults

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ installed
- Terminal/Command Prompt access

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your images:**
   - Place images in the `input/` folder
   - Supported: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`

3. **Run from anywhere** *(if alias is set up)*:
   ```bash
   mami-image
   ```

   **Or run locally:**
   ```bash
   ./mami-image
   ```

## 📖 How to Use

### Step-by-Step Workflow

The application guides you through these steps:

#### 1. **Image Discovery**
Shows all compatible images found in the input folder with file details

#### 2. **Processing Mode Selection**
Choose how you want to process your images:
- Press **Enter** for Convert Only (recommended)
- Or select specific compression/conversion modes

#### 3. **Quality Settings** *(if compressing)*
- Press **Enter** for Medium Quality (80%)
- Or customize compression level

#### 4. **Format Selection** *(if converting)*
- Press **Enter** to keep original formats
- Or choose: JPEG, PNG, WebP, etc.

#### 5. **Filename Settings**
- Press **Enter** for "-compressed" suffix
- Or customize suffix or keep original names

#### 6. **Processing**
Watch real-time progress with detailed feedback and file size comparisons

## 💡 Usage Examples

### Convert PNG to JPEG
```bash
Mode: Convert Only
Format: JPEG
Result: image.png → image.jpg (in output folder)
```

### Compress Images by 50%
```bash
Mode: Compress Only
Quality: Medium (80%)
Result: photo.jpg → photo-compressed.jpg (smaller file)
```

### Convert to WebP with Compression
```bash
Mode: Compress + Convert
Quality: Medium (80%)
Format: WebP
Result: image.png → image-compressed.webp
```

### Custom Workflow
```bash
Mode: Convert Only
Format: PNG
Suffix: -converted
Result: photo.jpg → photo-converted.png
```

## 🗂️ Directory Structure

```
mami-image-compress-convert/
├── 📄 mami-image              # Main executable
├── 🐍 app.py                  # Python application
├── 📦 requirements.txt        # Dependencies (Pillow)
├── 📁 input/                  # 👈 Place your images here
├── 📁 output/                 # 👉 Processed images appear here
└── 📖 README.md              # This documentation
```

## 🎨 Terminal Preview

```
╔════════════════════════════════════════════════════════════╗
║                    🖼️  IMAGE COMPRESSOR  🖼️                 ║
╚════════════════════════════════════════════════════════════╝

📁 Found 3 image(s) in input folder:

  📸 1. vacation-photo.jpg
      📐 4032×3024 pixels | 💾 3.45 MB
  🖼️ 2. screenshot.png
      📐 1920×1080 pixels | 💾 2.10 MB
  📷 3. portrait.jpeg
      📐 2400×1600 pixels | 💾 1.85 MB

⚠️  Are these the correct images to process?
Continue? (y/n): y

⚙️  Processing Mode Selection

Choose processing mode:
  1. Compress + Convert
  2. Convert + Compress
  3. Compress Only
  4. Convert Only [RECOMMENDED]

Enter your choice (or press Enter): [ENTER]

📝 Output Format Selection

Select output format:
  1. Keep Original [RECOMMENDED]
  2. JPEG (.jpg)
  3. PNG (.png)
  4. WebP (.webp)

Enter your choice (or press Enter): 4

📝 Output Filename Settings

Choose output filename format:
  1. Add suffix to filename [RECOMMENDED]
  2. Keep original filename

Enter your choice (or press Enter): [ENTER]

Suffix (press Enter for '-converted'): -webp

🔄 Processing images: Convert Only → WebP

[████████████████████████████████████████████████████] 100.0% (3/3)

📸 Processing: vacation-photo.jpg
   ✅ Success: 3.45MB → 2.12MB (38.5% reduction)
   💾 Saved as: vacation-photo-webp.webp

📊 Processing Summary:
   ✅ Successfully processed: 3
   💾 Total size reduction: 42.3%

🎉 Processing completed! Check the output folder.
```

## 🚀 Ways to Contribute

### 🐛 Bug Reports
- Use the GitHub Issues tab
- Include steps to reproduce
- Mention your OS and Python version
- Attach sample images if relevant (without personal data)

### 💡 Feature Requests
- Describe the feature and its use case
- Explain why it would be valuable
- Consider if it fits the project's scope

### 🔧 Code Contributions
- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Make your changes
- Test thoroughly
- Commit with clear messages
- Push and create a Pull Request

## ❓ FAQ

**Q: Will this overwrite my original images?**
A: No! Original images stay safe in the `input/` folder. Processed images go to `output/`.

**Q: What happens if I run out of space?**
A: The tool shows file sizes before processing. You can skip large files if needed.

**Q: Can I undo changes?**
A: Since originals are preserved, you can always restart with different settings.

**Q: How do I convert just one image?**
A: Put the single image in the `input/` folder and run normally.

**Q: What's the difference between the processing modes?**
A:
- **Convert Only**: Changes format without quality loss
- **Compress Only**: Reduces file size without changing format
- **Compress + Convert**: Reduces quality first, then changes format
- **Convert + Compress**: Changes format first, then reduces quality

## 🛠️ Troubleshooting

**"No module named PIL"**
```bash
pip install Pillow
```

**"Permission denied"**
```bash
chmod +x mami-image
```

**"No images found"**
- Check that images are in the `input/` folder
- Verify file formats are supported (.jpg, .png, .bmp, .tiff, .webp)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Security Policy

We take security seriously. Please report any vulnerabilities to [engineering@mamiteam.com](mailto:engineering@mamiteam.com).

**Last updated**: September 2025

---


## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- 🐛 Reporting bugs
- 💡 Suggesting features
- 🔧 Submitting code changes
- 📝 Improving documentation

### Quick Contribution Steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🌟 Show Your Support

If this project helped you, please:
- ⭐ Star the repository
- 🐛 Report any issues you find
- 💡 Suggest improvements
- 📢 Share it with others

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/mamitech/mami-image-compress-convert)
![GitHub forks](https://img.shields.io/github/forks/mamitech/mami-image-compress-convert)
![GitHub issues](https://img.shields.io/github/issues/mamitech/mami-image-compress-convert)
![GitHub license](https://img.shields.io/github/license/mamitech/mami-image-compress-convert)
![Python version](https://img.shields.io/badge/python-3.7%2B-blue)

---

**Made with ❤️ by Mamikos Engineering Team for the open source community**

*Happy image processing! 📸✨*

## 📧 Contact

For questions, support, or collaboration opportunities, reach out to us:
- **Email**: engineering@mamiteam.com
- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and community chat

Built with [Pillow](https://pillow.readthedocs.io/) for robust image processing.
