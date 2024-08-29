import React from 'react';

function Header() {
  return (
    <header className="bg-black text-white px-0 py-4">
      <div className="container mx-auto px-4 sm:px-6 lg:px-0">
        <div className="flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="none"
              stroke="url(#logo-gradient)"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="w-8 h-8 animate-gradient-x"
            >
              <defs>
                <linearGradient id="logo-gradient" x1="0%" y1="0%" x2="100%" y2="0%" gradientTransform="rotate(0)">
                  <stop offset="0%" stopColor="#71717a" />
                  <stop offset="50%" stopColor="#d4d4d8" />
                  <stop offset="100%" stopColor="#71717a" />
                </linearGradient>
              </defs>
              <path d="M20 5H9l-7 7 7 7h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2Z" />
              <line x1="18" y1="9" x2="12" y2="15" />
              <line x1="12" y1="9" x2="18" y2="15" />
            </svg>
            <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-zinc-500 via-zinc-300 to-zinc-500 animate-gradient-x">
               Weber
            </h1>
          </div>
          <nav className="ml-auto">
            <ul className="flex space-x-4">
              <li><a href="/home" className="text-zinc-400 hover:text-white transition-colors">Home</a></li>
              <li><a href="/features" className="text-zinc-400 hover:text-white transition-colors">Features</a></li>
              <li><a href="/about" className="text-zinc-400 hover:text-white transition-colors">About</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}

export default Header;