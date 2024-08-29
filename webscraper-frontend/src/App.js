import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import WebScraperForm from './components/WebScraperForm';

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow ">
        <WebScraperForm />
      </main>
      <Footer />
    </div>
  );
}

export default App;