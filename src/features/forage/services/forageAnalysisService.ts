import { LatLng } from "react-native-maps";

export interface ForageResult {
  probability: number;
  depth: string;
  flow: string;
  soilType: string;
  aquifer: string;
  recommendation: string;
}

export async function analyzeForage(coord: LatLng): Promise<ForageResult> {
  try {
    const response = await fetch("http://192.168.11.156:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        lat: coord.latitude,
        lon: coord.longitude,
      }),
    });

    const data = await response.json();

    console.log("API RESPONSE:", data); // 🔥 DEBUG

    // ❗ vérifier erreur backend
    if (!data.probability) {
      throw new Error("No probability returned");
    }

    const probability = Math.round(data.probability * 100);

    return {
      probability,
      depth: "N/A",
      flow: "N/A",
      soilType: "AI Model",
      aquifer: "Satellite",
      recommendation:
        probability > 70
          ? "Très bon endroit"
          : probability > 40
          ? "Potentiel moyen"
          : "Faible potentiel",
    };

  } catch (error) {
    console.error("ERROR FRONT:", error);

    return {
      probability: 0,
      depth: "Erreur",
      flow: "Erreur",
      soilType: "Erreur",
      aquifer: "Erreur",
      recommendation: "Erreur API",
    };
  }
}