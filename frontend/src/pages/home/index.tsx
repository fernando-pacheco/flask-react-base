import { ButtonCard } from "@/components/molecules/button-card"
import { useNavigate } from "react-router-dom"

export function Home() {
    const navigate = useNavigate()

    return (
        <div className="flex flex-1 w-full h-screen justify-center items-center">
            <ButtonCard
                action={() => navigate("/")}
                text="Redirecionar para tela inicial"
            />
        </div>
    )
}
