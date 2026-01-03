"""
Data Utilities for Student Exam Analysis

This module contains helper functions for data loading, processing, and analysis.
Useful for extending the main analysis with custom data or additional statistics.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


def calculate_student_statistics(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate various statistics for each student.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame with student names and exam scores
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with student statistics including average, min, max, std
    """
    numeric_cols = dataframe.select_dtypes(include=[np.number]).columns
    
    stats = pd.DataFrame()
    stats['Student'] = dataframe['Student']
    stats['Average'] = dataframe[numeric_cols].mean(axis=1)
    stats['Min Score'] = dataframe[numeric_cols].min(axis=1)
    stats['Max Score'] = dataframe[numeric_cols].max(axis=1)
    stats['Std Dev'] = dataframe[numeric_cols].std(axis=1)
    
    return stats


def get_top_performers(dataframe: pd.DataFrame, subject: str = None, top_n: int = 3) -> pd.DataFrame:
    """
    Get the top performing students in a subject or overall average.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame with student names and exam scores
    subject : str, optional
        Subject name for which to get top performers. If None, uses average score
    top_n : int
        Number of top performers to return (default: 3)
        
    Returns:
    --------
    pd.DataFrame
        DataFrame of top performers sorted by score (descending)
    """
    if subject is None:
        numeric_cols = dataframe.select_dtypes(include=[np.number]).columns
        dataframe = dataframe.copy()
        dataframe['Average'] = dataframe[numeric_cols].mean(axis=1)
        return dataframe[['Student', 'Average']].nlargest(top_n, 'Average')
    else:
        if subject not in dataframe.columns:
            raise ValueError(f"Subject '{subject}' not found in dataset")
        return dataframe[['Student', subject]].nlargest(top_n, subject)


def get_bottom_performers(dataframe: pd.DataFrame, subject: str = None, bottom_n: int = 3) -> pd.DataFrame:
    """
    Get the bottom performing students in a subject or overall average.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame with student names and exam scores
    subject : str, optional
        Subject name for which to get bottom performers. If None, uses average score
    bottom_n : int
        Number of bottom performers to return (default: 3)
        
    Returns:
    --------
    pd.DataFrame
        DataFrame of bottom performers sorted by score (ascending)
    """
    if subject is None:
        numeric_cols = dataframe.select_dtypes(include=[np.number]).columns
        dataframe = dataframe.copy()
        dataframe['Average'] = dataframe[numeric_cols].mean(axis=1)
        return dataframe[['Student', 'Average']].nsmallest(bottom_n, 'Average')
    else:
        if subject not in dataframe.columns:
            raise ValueError(f"Subject '{subject}' not found in dataset")
        return dataframe[['Student', subject]].nsmallest(bottom_n, subject)


def normalize_scores(scores: np.ndarray, method: str = 'minmax') -> np.ndarray:
    """
    Normalize scores using specified method.
    
    Parameters:
    -----------
    scores : np.ndarray
        Array of scores to normalize
    method : str
        Normalization method ('minmax' for 0-1 range, 'zscore' for standardization)
        
    Returns:
    --------
    np.ndarray
        Normalized scores
    """
    if method == 'minmax':
        return (scores - scores.min()) / (scores.max() - scores.min())
    elif method == 'zscore':
        return (scores - scores.mean()) / scores.std()
    else:
        raise ValueError(f"Unknown normalization method: {method}")


def get_subject_statistics(dataframe: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    """
    Get comprehensive statistics for each subject.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame with exam scores
        
    Returns:
    --------
    dict
        Dictionary with subject names as keys and statistics dictionaries as values
    """
    numeric_cols = dataframe.select_dtypes(include=[np.number]).columns
    
    stats = {}
    for subject in numeric_cols:
        stats[subject] = {
            'mean': dataframe[subject].mean(),
            'median': dataframe[subject].median(),
            'std': dataframe[subject].std(),
            'min': dataframe[subject].min(),
            'max': dataframe[subject].max(),
            'q1': dataframe[subject].quantile(0.25),
            'q3': dataframe[subject].quantile(0.75)
        }
    
    return stats
