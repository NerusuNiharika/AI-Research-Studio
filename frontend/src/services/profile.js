import api from "./api";

export const getResearchHistory = async () => {

    const response = await api.get("/profile/history");

    return response.data;

};