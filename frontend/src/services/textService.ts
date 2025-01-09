const baseURL = import.meta.env.VITE_BASE_URL;

async function get_sentiment(text: string) {
    const response = await fetch(baseURL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_input: text })
    });

    if (!response.ok) {
        throw new Error(`Error: ${response.status}`)
    }

    const data = await response.json();
    return data;
}

export default get_sentiment;