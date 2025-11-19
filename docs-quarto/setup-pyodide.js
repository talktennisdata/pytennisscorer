// Custom Pyodide setup for pytennisscorer
async function setupPyodide(pyodide) {
  console.log('Setting up Pyodide for pytennisscorer...');

  // Install micropip for package management
  await pyodide.loadPackage('micropip');
  const micropip = pyodide.pyimport('micropip');

  // Install pytennisscorer from PyPI
  try {
    await micropip.install('pytennisscorer');
    console.log('✅ Successfully installed pytennisscorer from PyPI');
  } catch (error) {
    console.error('❌ Error installing pytennisscorer:', error);
    console.warn('Live code examples may not work properly');
  }

  // Pre-import common modules to speed up execution
  await pyodide.runPythonAsync(`
    # Import pytennisscorer modules
    try:
        from pytennisscorer import TennisScorer, MatchType
        from pytennisscorer.models import MatchState, SetState, GameState
        from pytennisscorer.configs import create_match_config
        print("✅ pytennisscorer loaded successfully")
    except ImportError as e:
        print(f"⚠️ Could not import pytennisscorer: {e}")
        print("You can still use the documentation, but live examples won't work")
  `);

  return pyodide;
}

// Export for Quarto-live
window.setupPyodide = setupPyodide;