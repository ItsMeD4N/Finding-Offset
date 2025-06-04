# 🧠 Finding Offset - Binary Exploitation Helper

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)

**Finding Offset** is a Python-based CLI utility to assist with determining buffer overflow offset values, a crucial step in binary exploitation and Capture The Flag (CTF) challenges. The tool helps exploit developers identify the exact position in memory where their input overwrites critical registers like EIP/RIP.

## 🚀 Features

- Generate unique cyclic patterns
- Automatically find offset from crash value
- Compatible with GDB and pwndbg
- Simple and beginner-friendly interface
- Lightweight and fast

## 📦 Requirements

- Python 3.6+
- No external libraries required

## ⚙️ Usage

### 1. Generate a cyclic pattern:

```bash
python offset.py generate 200
```

This will generate a unique 200-byte cyclic pattern.

### 2. Find offset from crash value:

```bash
python offset.py find 6161616c
```

This will return the position (offset) of the pattern in the generated buffer.

> 💡 You can obtain the crash value from `EIP`, `RIP`, or from core dumps in GDB using tools like `pwndbg` (`pattern_create` and `pattern_offset` equivalents).

## 📁 Project Structure

```
Finding-Offset/
├── offset.py           # Main script
├── README.md
```

## 🤝 Contribution

Contributions are welcome!

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE)

## 📬 Contact

DAN – [@ItsMeD4N](https://github.com/ItsMeD4N)
