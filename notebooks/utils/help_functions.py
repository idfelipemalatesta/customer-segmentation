
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

def plot_silhouette_analysis(df_scaled, n_clusters, n_cols):
    """
    Gera o diagrama de silhouette.
    Se n_clusters for uma lista, gera os gráficos para cada valor com layout dinâmico.
    Se for um inteiro, gera o gráfico para esse valor.
    
    Utiliza sns.color_palette() para definir as cores dos clusters.
    """
    clusters = n_clusters if isinstance(n_clusters, list) else [n_clusters]
    n_plots = len(clusters)
    
    # Define o número de colunas (2 por padrão) e calcula as linhas necessárias
    cols = n_cols
    rows = math.ceil(n_plots / cols)
    
    fig, axs = plt.subplots(rows, cols, figsize=(14, 7))
    axs = axs.flatten()
    
    for idx, n in enumerate(clusters):
        ax1 = axs[idx]
        
        # Ajusta o modelo para n clusters
        kmeans = KMeans(n_clusters=n, init='k-means++', max_iter=1000, n_init=10, random_state=43)
        cluster_labels = kmeans.fit_predict(df_scaled)
        silhouette_avg = silhouette_score(df_scaled, cluster_labels)
        sample_silhouette_values = silhouette_samples(df_scaled, cluster_labels)
        
        # Define paleta de cores usando seaborn
        palette = sns.color_palette(n_colors=n)
        
        y_lower = 10
        for i in range(n):
            cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
            cluster_silhouette_values.sort()
            
            size_cluster_i = cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i
            
            ax1.fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_silhouette_values,
                              facecolor=palette[i], edgecolor=palette[i], alpha=0.7)
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
            y_lower = y_upper + 10
        
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
        ax1.set_title(f"{n} Clusters\nAvg Silhouette: {silhouette_avg:.2f}", size=10)
        #ax1.set_xlabel("Silhouette Coefficient")
        ax1.set_ylabel("Cluster Label")
        ax1.set_yticks([])
    
    # Remove eixos vazios se houver mais subplots que clusters
    for j in range(idx + 1, len(axs)):
        fig.delaxes(axs[j])
    
    plt.tight_layout()
    plt.show()