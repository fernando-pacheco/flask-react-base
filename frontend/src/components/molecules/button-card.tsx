import { Button } from "../atoms/button"

interface ButtonCardProps {
    text: string
    action: () => void
}

export function ButtonCard({ text, action }: ButtonCardProps) {
    return (
        <div className="p-10 bg-white rounded-lg">
            <Button
                className="bg-yellow-600 hover:bg-yellow-700"
                onClick={action}
            >
                {text}
            </Button>
        </div>
    )
}
