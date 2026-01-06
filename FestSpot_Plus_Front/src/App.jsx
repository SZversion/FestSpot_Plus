import RootLayout from "./components/layout/RootLayout/RootLayout";
import RootRouter from "./routes/RootRouter";

function App() {
  return (
    <>
      <RootLayout>
        <RootRouter />
      </RootLayout>
    </>
  );
}

export default App;
