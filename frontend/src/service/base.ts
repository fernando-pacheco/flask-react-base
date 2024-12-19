import { api } from "@/api"
import { AxiosError } from "axios"

export class BaseService {
    async get() {
        try {
            const response = await api.get("/cliente")
            return response
        } catch (error) {
            if (error instanceof AxiosError) {
                return error.response
            }

            return error
        }
    }
}
