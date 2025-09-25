# Contributing to Mami Image Compressor & Converter

Thank you for your interest in contributing to this project! 🎉

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

## 🛠️ Development Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Setup
```bash
# Clone your fork
git clone https://github.com/your-github-username/mami-image-compress-convert.git
cd mami-image-compress-convert

# Install dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x mami-image

# Test the installation
./mami-image
```

## 📝 Code Guidelines

### Style
- Follow PEP 8 Python style guide
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

### Testing
- Test with various image formats (JPEG, PNG, WebP, etc.)
- Test different processing modes
- Verify error handling
- Check edge cases (large files, corrupted images, etc.)

### Documentation
- Update README.md for new features
- Add docstrings to new functions
- Update help text if adding new options

## 🎯 Areas for Contribution

### High Priority
- [ ] Additional image formats (AVIF, HEIC, etc.)
- [ ] Progress bar improvements
- [ ] Memory optimization for large files
- [ ] Batch processing enhancements

### Medium Priority
- [ ] Configuration file support
- [ ] Drag-and-drop GUI wrapper
- [ ] More compression algorithms
- [ ] Metadata preservation options

### Low Priority
- [ ] Plugin system
- [ ] Cloud storage integration
- [ ] Advanced image filters
- [ ] Automated testing suite

## 🚦 Pull Request Process

1. **Before Starting**
   - Check existing issues and PRs
   - Discuss major changes first

2. **Development**
   - Create a feature branch
   - Write clean, tested code
   - Follow existing patterns

3. **Testing**
   - Test with multiple image types
   - Verify all processing modes work
   - Check error handling

4. **Documentation**
   - Update README if needed
   - Add code comments
   - Update help text

5. **Submission**
   - Clear commit messages
   - Reference related issues
   - Describe changes in PR

## 🔍 Code Review Criteria

- **Functionality**: Does it work as expected?
- **Safety**: No data loss or corruption?
- **Performance**: Efficient for large files?
- **Compatibility**: Works across platforms?
- **Style**: Follows project conventions?
- **Documentation**: Clear and complete?

## 🎨 UI/UX Guidelines

### Terminal Interface
- Use emojis consistently
- Maintain color scheme (Green=success, Red=error, Yellow=warning, Blue=info)
- Keep progress indicators clear
- Provide helpful error messages

### User Experience
- Default to safe options
- Show file size changes
- Confirm destructive operations
- Provide clear status updates

## 🏗️ Architecture

### File Structure
```
mami-image-compress-convert/
├── mami-image              # Main entry point
├── app.py                  # Core application logic
├── requirements.txt        # Python dependencies
├── input/                  # User image input
├── output/                 # Processed output
└── docs/                   # Documentation
```

### Key Classes
- `ImageCompressor`: Main application class
- `Colors`: Terminal color constants
- Processing methods: `_convert_format_only`, `_compress_quality_only`, etc.

### Processing Flow
1. Scan input folder
2. User confirmation
3. Mode/quality/format selection
4. Filename configuration
5. Image processing
6. Results summary

## 🤝 Community

### Communication
- Be respectful and constructive
- Help newcomers learn
- Share knowledge and experience
- Focus on the project's goals

### Recognition
- Contributors will be acknowledged
- Significant contributions may earn maintainer status
- All contributions are valued

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🆘 Getting Help

- **Questions**: Use GitHub Discussions
- **Bugs**: Create an Issue
- **Ideas**: Start a Discussion
- **Urgent**: Tag maintainers in Issues

---

**Happy Contributing! 🎉**

Together with the Mami Team, we can make image processing easier for everyone!

## 📧 Contact

For questions about contributing:
- **Email**: engineering@mamiteam.com
- **GitHub Discussions**: Use for community questions
- **GitHub Issues**: For specific bugs or feature requests