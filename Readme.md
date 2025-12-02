# 🎬 MyMovieRepo - Movie Poster Generator

A Streamlit web application that generates beautiful, high-resolution movie posters using The Movie Database (TMDB) API.

## Features

- 🔍 Search for movies by title
- 🎨 Extract color palettes from movie posters
- 📐 Multiple canvas sizes (Default, A-series, iPhone)
- 🌓 Light and dark mode options
- 🖼️ Transparent background support
- 🔤 Custom font upload
- 📥 High-resolution downloadable posters

## Prerequisites

- Python 3.8 or higher
- TMDB API key (free)

## Getting Your TMDB API Key

1. Create a free account at [The Movie Database](https://www.themoviedb.org/signup)
2. Go to your account settings
3. Navigate to the [API section](https://www.themoviedb.org/settings/api)
4. Request an API key (choose "Developer" option)
5. Fill out the required information
6. Copy your API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/MyMovieRepo.git
cd MyMovieRepo
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Enter your TMDB API key in the sidebar

3. Search for a movie by title

4. Customize your poster settings:
   - Choose output style (light/dark/transparent)
   - Select canvas aspect ratio
   - Upload a custom font (optional)

5. Click "Generate Poster" and download your creation!

## Project Structure

```
MyMovieRepo/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── LICENSE                # MIT License
```

## Poster Layout

The generated poster includes:
- High-resolution movie poster image
- Color palette extracted from the poster
- Movie title
- Director name
- Top-billed cast members
- Release date
- Runtime
- Production company

## Technologies Used

- **Streamlit** - Web application framework
- **TMDB API** - Movie data and poster images
- **Pillow (PIL)** - Image processing
- **ColorThief** - Color palette extraction
- **Requests** - API calls

## API Rate Limits

TMDB API free tier includes:
- 40 requests every 10 seconds
- This should be more than sufficient for typical usage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This product uses the TMDB API but is not endorsed or certified by TMDB
- Movie data and images courtesy of [The Movie Database (TMDB)](https://www.themoviedb.org/)

## Roadmap

- [ ] Implement TMDB API integration
- [ ] Add movie search functionality
- [ ] Create poster generation functions
- [ ] Add multiple movie selection if search returns multiple results
- [ ] Implement caching for API calls
- [ ] Add more poster layout templates
- [ ] Support for TV shows

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/yourusername/MyMovieRepo/issues) on GitHub.

---

Made with ❤️ and Streamlit
