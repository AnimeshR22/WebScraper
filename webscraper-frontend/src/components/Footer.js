import React from 'react';

function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-black text-white py-2">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
        </div>
        <div className="mt-8 text-center text-zinc-400 animate-gradient-x">
          <div className="flex items-center justify-center ">
          <h1 className="bg-clip-text font-bold text-transparent bg-gradient-to-r from-zinc-500 via-zinc-400 to-zinc-500 animate-gradient-x">&copy;{currentYear}Weber.</h1>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
