import { Home } from "@/pages/home"
import { Inicial } from "@/pages/inicial"
import { Route, Routes } from "react-router-dom"

export function AppRoutes() {
    return (
        <div>
            <Routes>
                <Route path="/home" element={<Home />} />
                <Route path="/" element={<Inicial />} />
            </Routes>
        </div>
    )
}
